# Part 3 · Improve the Python

:::{important}
## 🔀 Switch Repos Before Starting Part 3

Part 3 uses **`edgar-improve`** — the repo that starts with the pre-built `edgar_analysis.py`. If you've been working in `edgar-scratch` for Parts 1 and 2, switch now.

**In Terminal B:**
```bash
cd ~/copilot_dir/repos/edgar-improve
git log --oneline   # should show: "chore: initial commit with EDGAR starter code"
```

**In Terminal A — stop the current agent and restart it in `edgar-improve`:**

```bash
# Stop current agent: Ctrl+C  (Claude Code)  or  /exit  (Copilot CLI)

# Then restart:
cd ~/copilot_dir/repos/edgar-improve
ai_agent_container -a claude ~/copilot_dir/      # Claude Code
# or
ai_agent_container -a copilot ~/copilot_dir/     # Copilot CLI
```

All Terminal B commands for Parts 3 and 4 run from `~/copilot_dir/repos/edgar-improve`.
:::

---

## Goal

In this part, you will iteratively improve `starter-code/edgar_analysis.py` using four focused AI interactions — without changing what the script *does*.

This script processes **real SEC EDGAR Form 4 filings** from 2003, extracts insider buy/sell transactions, and writes a monthly summary. Your job is to make that pipeline easier to understand, test, reuse, and trust.

By the end of Part 3, your script will:

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
edgar-improve/
└── starter-code/
    ├── edgar_analysis.py              ← flat starter script (your starting point)
    └── output/
        └── insider_summary.csv        ← written by the script
```

## Ending State

```text
edgar-improve/
└── starter-code/
    ├── edgar_analysis.py              ← improved: logging + functions + argparse CLI
    ├── output/
    │   └── insider_summary.csv
    └── tests/
        └── test_edgar_analysis.py     ← new
```

With the default settings (`N_FILES=500`), the finished Python script should still produce the same 18-row monthly summary of `P` and `S` transactions for 2003.

---

**Start with [Step 1 – Understand](step1-understand.md) →**
