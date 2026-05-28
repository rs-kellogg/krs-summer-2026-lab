# Part 2 · Improve the Python

## Goal

In this part, you will iteratively improve `starter-code/edgar_analysis.py` using four focused AI interactions — without changing what the script *does*.

This script processes **real SEC EDGAR Form 4 filings** from 2003, extracts insider buy/sell transactions, and writes a monthly summary. Your job is to make that pipeline easier to understand, test, reuse, and trust.

By the end of Part 2, your script will:

- use Python's `logging` module instead of `print()`
- have its core XML-parsing and aggregation logic in named, testable functions
- be covered by a `pytest` test suite
- accept command-line arguments instead of hardcoded constants

## The Four Steps

| Step | What you ask the AI | What you get |
|------|-------------------|-------------|
| [Step 1 – Understand](step1-understand.md) | *Explain and critique* | A shared mental model of the Form 4 pipeline |
| [Step 2 – Add logging](step2-logging.md) | *Replace `print()` with structured logs* | A script that tells you what it's doing |
| [Step 3 – Refactor and test](step3-tests.md) | *Create functions + write pytest tests* | Modular code with a test suite |
| [Step 4 – Add a CLI](step4-cli.md) | *Add `argparse` options* | A configurable, reusable pipeline |

## Starting State

```text
starter-code/
├── edgar_analysis.py              ← flat starter script
└── output/
    └── insider_summary.csv        ← written by the script
```

## Ending State

```text
starter-code/
├── edgar_analysis.py              ← improved: logging + functions + argparse CLI
├── output/
│   └── insider_summary.csv
└── tests/
    └── test_edgar_analysis.py     ← new
```

With the default settings (`N_FILES=500`), the finished Python script should still produce the same 18-row monthly summary of `P` and `S` transactions for 2003.

---

**Start with [Step 1 – Understand](step1-understand.md) →**
