# Part 4, Step 2 – Write R Tests

## Mirror the Python Contract

Your R tests should check the same core behaviors as the Python tests:

1. parsing a minimal Form 4 filing extracts the right transaction
2. filtering keeps only `P` and `S`
3. summarizing by month produces correct row counts and totals

Using the **same minimal filing fixture** in both languages makes the cross-language verification direct: if both suites pass with the same inputs, you have strong evidence the logic is equivalent.

---

## Your Prompt

:::{admonition} 💬 Prompt — Write testthat tests for the R pipeline
:class: tip
```
Write testthat tests for starter-code/edgar_analysis.R that mirror the Python
tests in starter-code/tests/test_edgar_analysis.py.

Save the file as starter-code/tests/test_edgar_analysis.R.

Requirements:
- Use the same minimal Form 4 XML fixture as the Python tests
- Test that parse_filing() extracts a sale transaction with:
    transaction_code == "S"
    shares == 1000
    price_per_share == 25.50
- Test that filter_transactions() keeps only P and S rows
- Test that summarize_by_month() returns the correct row count and total_shares
- Source edgar_analysis.R using:
    SOURCED_FOR_TESTING <- TRUE
    source("starter-code/edgar_analysis.R")
```
:::

:::{note}
A good `starter-code/tests/test_edgar_analysis.R` will look something like:

```r
library(testthat)
library(dplyr)
library(tibble)

SOURCED_FOR_TESTING <- TRUE
source("starter-code/edgar_analysis.R")

MINIMAL_FILING <- '-----BEGIN PRIVACY-ENHANCED MESSAGE-----

<SEC-DOCUMENT>
<SEC-HEADER>
CONFORMED SUBMISSION TYPE: 4
</SEC-HEADER>
<DOCUMENT>
<TEXT>
<XML>
<ownershipDocument>
    <issuer>
        <issuerCik>0001000015</issuerCik>
        <issuerName>TEST CORP</issuerName>
    </issuer>
    <reportingOwner>
        <reportingOwnerId>
            <rptOwnerCik>0001234567</rptOwnerCik>
            <rptOwnerName>DOE JOHN</rptOwnerName>
        </reportingOwnerId>
        <reportingOwnerRelationship>
            <isDirector>1</isDirector>
            <isOfficer>0</isOfficer>
        </reportingOwnerRelationship>
    </reportingOwner>
    <nonDerivativeTable>
        <nonDerivativeTransaction>
            <transactionDate><value>2003-06-15</value></transactionDate>
            <transactionCoding>
                <transactionCode>S</transactionCode>
            </transactionCoding>
            <transactionAmounts>
                <transactionShares><value>1000</value></transactionShares>
                <transactionPricePerShare><value>25.50</value></transactionPricePerShare>
                <transactionAcquiredDisposedCode><value>D</value></transactionAcquiredDisposedCode>
            </transactionAmounts>
        </nonDerivativeTransaction>
    </nonDerivativeTable>
</ownershipDocument>
</XML>
</TEXT>
</DOCUMENT>
</SEC-DOCUMENT>
-----END PRIVACY-ENHANCED MESSAGE-----'


test_that("parse_filing extracts a sale transaction", {
  path <- tempfile(fileext = ".txt")
  writeLines(MINIMAL_FILING, path)
  rows <- parse_filing(path)

  expect_equal(nrow(rows), 1)
  expect_equal(rows$transaction_code[[1]], "S")
  expect_equal(rows$shares[[1]], 1000)
  expect_equal(rows$price_per_share[[1]], 25.50, tolerance = 1e-6)
})


test_that("filter_transactions keeps only P and S", {
  df <- tibble(
    transaction_code = c("S", "P", "A", "J"),
    shares = c(100, 200, 300, 400),
    price_per_share = c(10, 20, 30, 40)
  )
  filtered <- filter_transactions(df)

  expect_equal(filtered$transaction_code, c("S", "P"))
})


test_that("summarize_by_month returns correct counts and totals", {
  df <- tibble(
    transaction_date = as.Date(c("2003-06-01", "2003-06-15", "2003-07-02")),
    transaction_code = c("S", "S", "P"),
    shares = c(100, 150, 200),
    price_per_share = c(10, 12, 8),
    month = c("2003-06", "2003-06", "2003-07")
  )
  summary <- summarize_by_month(df)

  expect_equal(nrow(summary), 2)
  june_s <- filter(summary, month == "2003-06", transaction_code == "S")
  expect_equal(june_s$n_transactions[[1]], 2)
  expect_equal(june_s$total_shares[[1]], 250)
})
```
:::

---

## Run the R Tests

```bash
Rscript -e "testthat::test_file('starter-code/tests/test_edgar_analysis.R')"
```

Then re-run the Python tests to make sure nothing has drifted:

```bash
PYTHONPATH=starter-code pytest starter-code/tests/ -v
```

:::{admonition} Chat interface — verify without running
:class: seealso
Paste the generated `test_edgar_analysis.R` back and ask: *"Trace through `test_that('parse_filing extracts a sale transaction', ...)`. What does `parse_filing()` return for the MINIMAL_FILING? Do the three `expect_equal` assertions pass?"*

Then compare the R test fixture to the Python `MINIMAL_FILING` string — they should be identical. Ask: *"Do the Python and R tests use the same fixture? Why does that matter for cross-language validation?"*
:::

---

## Commit

```bash
git add starter-code/tests/test_edgar_analysis.R
git commit -m "test: add R testthat suite for EDGAR pipeline"
```

:::{important}
- [ ] `starter-code/tests/test_edgar_analysis.R` exists
- [ ] All three R tests pass
- [ ] All three Python tests still pass
- [ ] You now have matching test coverage in both languages
:::

---

**Next: [Step 3 – Compare Outputs and Fix Divergences](step3-fix-refactor.md) →**
