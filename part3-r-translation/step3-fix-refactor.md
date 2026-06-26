# Part 4, Step 3 – Compare Outputs and Fix Divergences

## Now Verify the Translation End-to-End

Passing unit tests is necessary, but not sufficient. You also need to compare the **full pipeline outputs** from Python and R.

Both scripts should produce the same 18 monthly rows when run against the same 500 filings.

---

## Run Both Scripts

::::{tab-set}
:::{tab-item} Chat Interface
Paste both `edgar_analysis.py` and `edgar_analysis.R` into the conversation and ask:

*"Compare how Python and R handle these three things: (1) stripping whitespace from XML text values, (2) NaN vs NA for missing prices when written to CSV, and (3) rounding to 2 decimal places. Would the outputs match row-for-row, or are there likely differences?"*

Use the answer to guide which fixes to apply before proceeding.
:::
:::{tab-item} CLI Tools
```bash
python starter-code/edgar_analysis.py
Rscript starter-code/edgar_analysis.R
```

Then compare the outputs side by side:

```bash
cat starter-code/output/insider_summary.csv
cat starter-code/output/insider_summary_r.csv
```
:::
::::

With the defaults, both should match this reference:

```text
month,transaction_code,n_transactions,total_shares,mean_price
2003-01,P,1,4008030.0,
2003-04,P,2,0.0,0.0
2003-04,S,1,100.0,5.0
2003-05,P,12,44383.0,10.27
2003-05,S,29,260159.0,27.67
2003-06,P,7,5683.0,14.32
2003-06,S,47,606940.0,15.37
2003-07,P,10,11250.0,6.03
2003-07,S,10,46300.0,4.32
2003-08,P,35,699566.0,4.65
2003-08,S,6,30200.0,23.9
2003-09,P,7,7547.0,12.97
2003-09,S,39,259050.0,3.17
2003-10,P,1,43000.0,6.54
2003-10,S,22,50698.0,4.73
2003-11,P,14,31555.0,17.77
2003-11,S,45,201885.0,51.7
2003-12,S,37,570720.0,19.8
```

---

## Your Prompt

:::{admonition} 💬 Prompt — Compare outputs and fix mismatches
:class: tip
```
Compare starter-code/output/insider_summary.csv and
starter-code/output/insider_summary_r.csv.

If they differ, identify the rows that don't match and fix the R script
so it produces the same output as Python.

Pay special attention to:
- XML whitespace (R may include leading/trailing spaces from xml_text())
- NaN vs NA for missing prices (use NA_real_ before writing CSV)
- factor vs character behavior for month columns
- How dplyr rounds vs Python's round()

After fixing any divergences, confirm that all R tests still pass.
```
:::

:::{note}
Common Python-vs-R gotchas in this lab:

| Issue | Python behavior | R gotcha |
|-------|----------------|----------|
| **XML whitespace** | `.strip()` on all values | `xml_text()` may keep surrounding spaces — use `trimws()` |
| **Missing price mean** | `NaN` in CSV (empty cell) | `mean(..., na.rm=TRUE)` returns `NaN` for all-NA groups; use `ifelse(is.nan(.), NA, .)` |
| **Month column type** | character | `format(as.Date(...))` produces character — don't convert to factor |
| **Rounding** | `round(2)` | `round()` in R rounds 0.5 to nearest even — use `janitor::round_half_up()` if needed |

These are exactly the kind of subtle cross-language issues that tests and output comparison reveal.
:::

:::{admonition} 🗣️ Discussion — What can tests catch, and what can't they?
:class: seealso
Both the Python and R pipelines pass their unit tests, but produce different numbers from the real data. What does that tell you about what unit tests can and can't catch?
:::

---

## Re-Run Everything

After fixing any mismatches, run all checks:

```bash
PYTHONPATH=starter-code pytest starter-code/tests/ -v
Rscript -e "testthat::test_file('starter-code/tests/test_edgar_analysis.R')"
python starter-code/edgar_analysis.py
Rscript starter-code/edgar_analysis.R
```

If everything is correct:

- All Python tests pass
- All R tests pass
- `insider_summary.csv` and `insider_summary_r.csv` match row-for-row

---

## Final Commit

```bash
git add starter-code/edgar_analysis.R \
        starter-code/output/insider_summary_r.csv \
        starter-code/tests/test_edgar_analysis.R
git commit -m "feat: align R EDGAR pipeline with Python output"
```

:::{important}
- [ ] The Python and R monthly summaries match row-for-row
- [ ] All Python tests pass
- [ ] All R tests pass
- [ ] You fixed any XML whitespace, missing-value, or type differences
- [ ] Your git history tells the story: translate → test → compare → fix
:::

---

**Optional: [Bonus · Parallelization](../part4-bonus.md) →**

**Or skip to: [Wrap-Up](../wrap-up.md) →**
