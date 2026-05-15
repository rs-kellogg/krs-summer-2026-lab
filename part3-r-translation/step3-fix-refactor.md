# Part 3, Step 3 – Fix Discrepancies & Refactor

## Two Tasks, One Step

Now you'll do two things:

1. **Fix the test failure** — use the AI to diagnose and repair the R function so all tests pass
2. **Make both scripts configurable** — replace hardcoded paths with command-line arguments

---

## Task A: Fix the Test Failure

:::{admonition} 💬 Prompt — Fix the R function
:class: tip
```
My R test for summarize_by_year() is failing because rounding behaves differently
than in the Python version. The Python uses df.round(4) on the final DataFrame.
The R version uses mutate(across(where(is.double), ~round(.x, 4))).

Please fix the R summarize_by_year() function so that the rounding matches Python's
behavior. Make sure the fix doesn't break the other two tests.
```
:::

After the fix, run the tests again:

```bash
Rscript -e "testthat::test_file('starter-code/tests/test_firm_analysis.R')"
```

All three should now pass:

```
✔ | 3 | test_firm_analysis.R
```

:::{note}
The typical fix is ensuring that rounding happens after all aggregation is complete, and applying it consistently. The AI will identify the specific cause based on your version of the code.
:::

---

## Task B: Remove Hardcoded Paths

Both scripts still hardcode their input/output paths. This makes them useless for anyone with a different directory structure — including you six months from now on a different machine.

:::{admonition} 💬 Prompt — Add CLI arguments to Python
:class: tip
```
Add argparse command-line arguments to starter-code/firm_analysis.py so that
users can specify:
  --input PATH      Path to the input CSV (default: starter-code/data/firms.csv)
  --output PATH     Path to the output CSV (default: starter-code/output/summary.csv)
  --min-revenue N   Revenue threshold for filtering (default: 1000000)

The defaults should match the current hardcoded values so existing behavior is
unchanged. Log each argument value at the INFO level at startup.
```
:::

:::{admonition} 💬 Prompt — Add CLI arguments to R
:class: tip
```
Add command-line argument parsing to starter-code/firm_analysis.R using the
optparse package, with the same three arguments:
  --input PATH      (default: starter-code/data/firms.csv)
  --output PATH     (default: starter-code/output/summary_r.csv)
  --min-revenue N   (default: 1000000)

Print each argument value to the console at startup using message().
```
:::

---

## Test That the Defaults Still Work

```bash
# Python — should behave exactly as before
python starter-code/firm_analysis.py

# With explicit arguments
python starter-code/firm_analysis.py \
  --input starter-code/data/firms.csv \
  --output starter-code/output/summary.csv \
  --min-revenue 2000000

# R — should behave exactly as before
Rscript starter-code/firm_analysis.R

# With explicit arguments
Rscript starter-code/firm_analysis.R \
  --input starter-code/data/firms.csv \
  --output starter-code/output/summary_r2m.csv \
  --min-revenue 2000000
```

Re-run both test suites to confirm nothing broke:

```bash
PYTHONPATH=starter-code pytest starter-code/tests/test_firm_analysis.py -v
Rscript -e "testthat::test_file('starter-code/tests/test_firm_analysis.R')"
```

---

## Final Commit

```bash
git add starter-code/firm_analysis.py starter-code/firm_analysis.R
git commit -m "feat: add argparse/optparse CLI arguments, fix R rounding"
```

:::{important}
- [ ] All Python tests pass
- [ ] All R tests pass
- [ ] Both scripts accept `--input`, `--output`, and `--min-revenue` arguments
- [ ] Running both scripts with no arguments produces the same output as before
- [ ] Your git log shows a clear history of incremental improvements
:::

---

**Optional: [Bonus · Parallelization](../part4-bonus.md) →**

**Or skip to: [Wrap-Up](../wrap-up.md) →**
