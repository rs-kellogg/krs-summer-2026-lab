# Part 2 · Improve the Python

## Goal

In this part, you will iteratively improve `starter-code/firm_analysis.py` using four focused AI interactions — without changing what the script *does*.

By the end of Part 2, your script will:

- Use Python's `logging` module instead of `print()`
- Have its core calculations in named, testable functions
- Be covered by a `pytest` test suite
- Accept command-line arguments instead of hardcoded paths

## The Four Steps

| Step | What you ask the AI | What you get |
|------|-------------------|-------------|
| [Step 1 – Understand](step1-understand.md) | *Explain and critique* | A shared vocabulary for what the code does |
| [Step 2 – Add logging](step2-logging.md) | *Add structured logging* | A script that tells you what it's doing |
| [Step 3 – Add unit tests](step3-tests.md) | *Refactor + write pytest tests* | Modular code with a test suite |
| [Step 4 – Add a CLI](step4-cli.md) | *Add argparse arguments* | A configurable, reusable pipeline |

## Starting State

```
starter-code/
├── data/
│   └── firms.csv        ← 250 rows of synthetic firm-year data
├── output/
│   └── (empty)
└── firm_analysis.py     ← your starting point
```

## Ending State

```
starter-code/
├── data/
│   └── firms.csv
├── output/
│   └── summary.csv
├── firm_analysis.py     ← improved: logging + functions + argparse CLI
└── tests/
    └── test_firm_analysis.py   ← new
```

---

**Start with [Step 1 – Understand](step1-understand.md) →**
