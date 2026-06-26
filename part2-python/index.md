# Example: Improve a Script

## What You're Doing and Why

You have a working Python script — `starter-code/edgar_analysis.py` — that parses real SEC EDGAR Form 4 filings and writes a monthly summary of insider buy/sell transactions.

It works. But it has the same problems that most research scripts have: `print()` instead of logging, no functions, no tests, hardcoded paths. This example walks through fixing all four, one focused AI interaction at a time.

**By the end, your script will embody all four pillars:**

| Pillar | What changes |
|--------|-------------|
| **Logging** | `print('done')` → timestamped INFO lines with counts and paths |
| **Testing** | Flat script → named functions covered by a pytest suite |
| **Abstraction** | Tangled logic → `parse_filing()`, `filter_transactions()`, `summarize_by_month()` |
| **Automation** | Hardcoded constants → `--data-dir`, `--output`, `--n-files` CLI arguments |

The script processes the same data throughout — what changes is how trustworthy, readable, and reusable it is.

---

:::{note}
**If you're jumping directly to this example:** the starter script is at `starter-code/edgar_analysis.py` in the lab repo. Chat interface users: open [Step 1](step1-understand.md), expand the script dropdown, and paste it into your conversation before starting.

**If you're coming from the Explore example:** the script you built there and this starter script do the same thing. You can work through these steps using either one.
:::

---

## The Four Steps

| Step | Pillar | What you do |
|------|--------|-------------|
| [Step 1 – Understand the code](step1-understand.md) | — | Read and critique before changing anything |
| [Step 2 – Add logging](step2-logging.md) | **Logging** | Replace `print()` with structured log output |
| [Step 3 – Refactor and test](step3-tests.md) | **Testing + Abstraction** | Extract functions, write pytest tests |
| [Step 4 – Add a CLI](step4-cli.md) | **Automation** | Make the script configurable at runtime |

---

:::{admonition} CLI Tools — switch repos before starting
:class: note
This example uses **`edgar-improve`** — the repo that starts with the pre-built `edgar_analysis.py`.

```bash
cd ~/copilot_dir/repos/edgar-improve
git log --oneline   # should show: "chore: initial commit with EDGAR starter code"
```

Restart your AI agent from this directory before proceeding.
:::

---

**Start with [Step 1 – Understand the code](step1-understand.md) →**
