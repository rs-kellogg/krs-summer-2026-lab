# Part 4, Step 1 – Translate to R

## Translate the Same Pipeline, Not a New One

The R version should do the same job as the Python version:

- read EDGAR Form 4 filing text files
- extract the embedded `<ownershipDocument>` XML
- handle both XML schema variants (X0101 and X0201)
- keep only non-derivative `P` and `S` transactions
- summarize by `month` and `transaction_code`
- write `starter-code/output/insider_summary_r.csv`

---

## Your Prompt

:::{admonition} 💬 Prompt — Translate edgar_analysis.py to R
:class: tip
```
Translate starter-code/edgar_analysis.py to R.

Requirements:
- Use xml2::read_xml() to parse the extracted XML string
- Use dplyr for data manipulation
- Use readr::write_csv() for output
- Use purrr::map_dfr() to iterate over filing files
- Keep the same function structure:
    parse_filing(filepath)
    filter_transactions(df, codes = c("P", "S"))
    summarize_by_month(df)
    main()
- Make parse_filing() handle both nonDerivativeTransaction (X0201)
  and nonDerivativeSecurity (X0101) elements
- Write output to starter-code/output/insider_summary_r.csv
- Guard main() with:
    if (!interactive() && !exists("SOURCED_FOR_TESTING")) main()
  so the file is safe to source() from tests

Please add brief comments for Python users who are new to R.
```
:::

:::{note}
The translated R file should use patterns like these for XML parsing:

```r
library(xml2)
library(dplyr)
library(readr)
library(purrr)
library(stringr)

parse_filing <- function(filepath) {
  content <- readLines(filepath, warn = FALSE) |> paste(collapse = "\n")

  # Extract the ownershipDocument XML block
  xml_block <- str_match(content, "(?s)(<ownershipDocument>.*?</ownershipDocument>)")[, 2]
  if (is.na(xml_block)) return(tibble())

  doc <- tryCatch(read_xml(xml_block), error = function(e) NULL)
  if (is.null(doc)) return(tibble())

  issuer_name <- xml_text(xml_find_first(doc, ".//issuerName"))
  issuer_cik  <- xml_text(xml_find_first(doc, ".//issuerCik"))
  owner_name  <- xml_text(xml_find_first(doc, ".//rptOwnerName"))
  is_director <- xml_text(xml_find_first(doc, ".//isDirector")) == "1"
  is_officer  <- xml_text(xml_find_first(doc, ".//isOfficer"))  == "1"

  # X0201 schema uses nonDerivativeTransaction; X0101 uses nonDerivativeSecurity
  txns <- xml_find_all(doc, ".//nonDerivativeTransaction")
  if (length(txns) == 0) txns <- xml_find_all(doc, ".//nonDerivativeSecurity")

  # ...extract fields from each transaction node...
}

filter_transactions <- function(df, codes = c("P", "S")) {
  filter(df, transaction_code %in% codes)
}

summarize_by_month <- function(df) {
  df %>%
    group_by(month, transaction_code) %>%
    summarise(
      n_transactions = n(),
      total_shares   = sum(shares, na.rm = TRUE),
      mean_price     = mean(price_per_share, na.rm = TRUE),
      .groups = "drop"
    ) %>%
    mutate(mean_price = ifelse(is.nan(mean_price), NA_real_, mean_price)) %>%
    mutate(across(where(is.numeric), ~ round(.x, 2)))
}
```

Your exact code may differ, but it should use `xml2`, `dplyr`, `readr`, and `purrr` rather than base-R XML or apply loops.
:::

---

## Run It

::::{tab-set}
:::{tab-item} CLI Tools
```bash
Rscript starter-code/edgar_analysis.R
```

Then inspect the output:

```bash
cat starter-code/output/insider_summary_r.csv
```
:::
:::{tab-item} Chat Interface
Paste the generated `edgar_analysis.R` back and ask: *"Does `parse_filing()` handle both the X0201 schema (`nonDerivativeTransaction`) and the X0101 schema (`nonDerivativeSecurity`)? Trace through what happens for each case."*

Also check: *"Is `main()` guarded by `if (!interactive() && !exists('SOURCED_FOR_TESTING'))`? Why does that matter for the R tests in Step 2?"*
:::
::::

It should have the same five columns as the Python output:

| Column | Description |
|--------|-------------|
| `month` | Year-month string (e.g., `2003-06`) |
| `transaction_code` | `P` (purchase) or `S` (sale) |
| `n_transactions` | Number of transactions that month |
| `total_shares` | Total shares transacted |
| `mean_price` | Average price per share |

:::{warning}
At this stage, the R output may differ slightly from Python. That is expected — Step 3 is where you reconcile the two.
:::

---

## Commit

```bash
git add starter-code/edgar_analysis.R
git commit -m "feat: add initial R translation of EDGAR pipeline"
```

:::{important}
- [ ] `starter-code/edgar_analysis.R` exists and runs without errors
- [ ] It uses `xml2`, `dplyr`, `readr`, and `purrr`
- [ ] It writes `starter-code/output/insider_summary_r.csv`
- [ ] The file is safe to `source()` from tests (guarded `main()`)
:::

---

**Next: [Step 2 – Write R Tests](step2-tests.md) →**
