# Part 3, Step 2 – Write R Tests

## The Contract Test

The tests you're about to write serve a specific purpose: **verify that the R functions produce the same results as the Python functions on the same input.**

To make this possible, you'll use the *exact same small DataFrame* that the Python tests use — just expressed in R syntax. If both test suites pass with the same inputs and expected outputs, the translation is verified.

---

## Your Prompt

:::{admonition} 💬 Prompt — Write R tests
:class: tip
```
Write a testthat test file for starter-code/firm_analysis.R.

Use the same test fixture as the Python tests — a small inline DataFrame with
these exact values:

  firm_id  year  revenue    cost       assets
  F001     2020  2000000    1200000    4000000
  F001     2021  3000000    1800000    5000000
  F002     2020  500000     350000     800000
  F002     2021  600000     420000     900000

Write tests that verify:
1. compute_metrics() returns correct profit_margin (F001 2020 should be 0.4)
2. filter_firms() with min_revenue=1000000 keeps only F001 rows (2 rows)
3. summarize_by_year() returns 2 rows and n_firms is 1 for each year

Save the file as starter-code/tests/test_firm_analysis.R
```
:::

:::{note}
```r
library(testthat)
library(dplyr)
source("starter-code/firm_analysis.R", local = TRUE)

sample_df <- tibble(
  firm_id = c("F001", "F001", "F002", "F002"),
  year    = c(2020L, 2021L, 2020L, 2021L),
  revenue = c(2e6, 3e6, 5e5, 6e5),
  cost    = c(1.2e6, 1.8e6, 3.5e5, 4.2e5),
  assets  = c(4e6, 5e6, 8e5, 9e5)
)

test_that("compute_metrics returns correct profit_margin", {
  result <- compute_metrics(sample_df)
  expect_equal(result$profit_margin[1], 0.4, tolerance = 1e-4)
})

test_that("filter_firms removes small firms", {
  df <- compute_metrics(sample_df)
  filtered <- filter_firms(df, min_revenue = 1e6)
  expect_equal(nrow(filtered), 2)
  expect_true(all(filtered$firm_id == "F001"))
})

test_that("summarize_by_year returns one row per year", {
  df <- filter_firms(compute_metrics(sample_df))
  summary <- summarize_by_year(df)
  expect_equal(nrow(summary), 2)
  expect_equal(summary$n_firms, c(1L, 1L))
})
```
:::

---

## Run the R Tests

```bash
Rscript -e "testthat::test_file('starter-code/tests/test_firm_analysis.R')"
```

:::{warning}
**A test will likely fail — this is expected and it's the point of the exercise.**

A common failure is in `summarize_by_year` — the `round()` behavior in R's `mutate(across(...))` can differ from pandas' `.round(4)` in edge cases involving ties or floating-point representation.

You may see something like:

```
── Failure: summarize_by_year returns one row per year ──
summary$mean_profit_margin[1] not equal to 0.4.
Actual: 0.4001
```

**Don't fix it yet** — understanding the failure is the next step.
:::

## Understanding the Failure

:::{admonition} 💬 Prompt — Diagnose the failure
:class: tip
```
My R test for summarize_by_year() is failing. The Python test expects
mean_profit_margin for 2020 to be 0.4 (after rounding to 4 decimal places),
but the R version is returning 0.4001.

Here is the R summarize_by_year function: [paste your function]

What is causing the discrepancy, and how should I fix it?
```
:::

---

## Commit What You Have

Even with a failing test, commit — the test file is valuable:

```bash
git add starter-code/tests/test_firm_analysis.R
git commit -m "test: add R testthat suite (one test failing — to be fixed)"
```

:::{important}
- [ ] `starter-code/tests/test_firm_analysis.R` exists
- [ ] You've run the tests and seen at least one failure
- [ ] You understand (conceptually) why the failure occurred
:::

---

**Next: [Step 3 – Fix & Refactor](step3-fix-refactor.md) →**
