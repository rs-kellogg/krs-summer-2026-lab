# Step 2 – Add Logging

## Why Logging Matters Here

When you run a script against hundreds of real SEC filings, `print('done')` is not enough.

You want to know:

- how many files were processed
- how many filings produced parse errors
- how many transactions were extracted
- how many rows remained after filtering to `P` and `S`
- where the final CSV was written and how many rows it contains

Python's built-in `logging` module gives you timestamps, severity levels, and much clearer progress reporting. When you submit this script as a SLURM job overnight, those log lines are what tell you whether it succeeded.

---

:::{admonition} 🗣️ Discussion — What would you want in a log?
:class: seealso
If this script ran overnight as a SLURM job and you came back to a finished run the next morning, what would you want to be able to know just from the output? What would you want to see in a log file?
:::

---

## Your Prompt

:::::{tab-set}
::::{tab-item} Chat Interface
:::{admonition} 💬 Prompt — Replace print statements with logging
:class: tip
```
Modify the script above to replace print() statements with Python's logging module.

Requirements:
- Use logging.basicConfig with INFO-level logging
- Log messages at INFO level should include:
  - "Processing N_FILES files from DATA_DIR"
  - "Extracted X transactions"
  - "Parse errors: Y files skipped"
  - "After filtering to P/S: Z rows"
  - "Summary written to OUTPUT_PATH (N rows)"
- Keep the existing behavior and output CSV format unchanged
- Do not refactor into functions yet
```
:::
::::
::::{tab-item} CLI Tools
:::{admonition} 💬 Prompt — Replace print statements with logging
:class: tip
```
Modify starter-code/edgar_analysis.py to replace print() statements with Python's
logging module.

Requirements:
- Use logging.basicConfig with INFO-level logging
- Log messages at INFO level should include:
  - "Processing N_FILES files from DATA_DIR"
  - "Extracted X transactions"
  - "Parse errors: Y files skipped"
  - "After filtering to P/S: Z rows"
  - "Summary written to OUTPUT_PATH (N rows)"
- Keep the existing behavior and output CSV format unchanged
- Do not refactor into functions yet
```
:::
::::
:::::

::::{note}
What matters is the **shape of the logging**, not the exact implementation.

Your INFO messages should look like:

```
2026-07-15 14:02:31,145 INFO Processing 500 files from /kellogg/data/EDGAR/4/2003
2026-07-15 14:02:55,012 INFO Extracted 539 transactions
2026-07-15 14:02:55,013 INFO Parse errors: 135 files skipped
2026-07-15 14:02:55,021 INFO After filtering to P/S: 334 rows
2026-07-15 14:02:55,025 INFO Summary written to starter-code/output/insider_summary.csv (18 rows)
```

Your exact counts will depend on how many filings parse successfully.

:::{warning}
If the AI wraps the main logic in an `if __name__ == '__main__':` block, that is correct — it's important for testability in Step 3.

If it doesn't, ask: *"Please wrap the main logic in an `if __name__ == '__main__':` block."*
:::
::::

---

## Run It

::::{tab-set}
:::{tab-item} Chat Interface
Ask: *"Based on the updated script, write out exactly what the five INFO log lines would look like when processing 500 files, assuming 135 parse errors and 539 transactions extracted. Use the timestamp format from `logging.basicConfig`."*

Then check that the code still writes `starter-code/output/insider_summary.csv` with the same groupby logic as before.
:::
:::{tab-item} CLI Tools
From the repo root — run the script and capture the log output to a file at the same time:

```bash
python starter-code/edgar_analysis.py 2>&1 | tee -a logs/edgar_analysis.log
```

`tee -a` writes to `logs/edgar_analysis.log` while still printing to the terminal so you can watch progress live. The `-a` flag appends, so successive runs accumulate a history rather than overwriting.

Create the `logs/` directory first if it doesn't exist:

```bash
mkdir -p logs
python starter-code/edgar_analysis.py 2>&1 | tee -a logs/edgar_analysis.log
```

Then inspect the log and verify the CSV output is unchanged:

```bash
cat logs/edgar_analysis.log
cat starter-code/output/insider_summary.csv
```

:::{tip}
`2>&1` redirects stderr to stdout so that both INFO log lines and any unexpected error output are captured together in the log file. Without it, only stdout is piped to `tee` and error messages disappear.
:::
:::
::::

---

## Commit

```bash
git add starter-code/edgar_analysis.py
git commit -m "feat: replace print with structured logging"
```

:::{important}
- [ ] Running the script now prints timestamped INFO messages
- [ ] The CSV output is still `starter-code/output/insider_summary.csv`
- [ ] The summary content is unchanged from before
- [ ] The logging change is committed to git
:::

---

**Next: [Step 3 – Refactor and Test](step3-tests.md) →**
