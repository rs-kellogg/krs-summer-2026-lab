# Copilot Instructions

## What This Repository Is

A **MyST Markdown static-site lab** — a 90-minute hands-on workshop where participants use AI coding assistants (GitHub Copilot CLI and Claude Code CLI) to improve a Python data analysis script, translate it to R, and add tests. The "code" participants actually write lives in `starter-code/`; the rest of the repo is documentation.

## Build

```bash
# Local preview
myst start

# Production build (mirrors CI)
BASE_URL="/krs-summer-2026-lab" myst build --html
# Output lands in _build/html/
```

CI (`.github/workflows/publish.yml`) builds and deploys to GitHub Pages on every push to `main`.

## Running the Starter Code

```bash
# Python pipeline
python starter-code/firm_analysis.py

# R pipeline (once created by lab participants)
Rscript starter-code/firm_analysis.R
```

## Tests

```bash
# All Python tests
PYTHONPATH=starter-code pytest starter-code/tests/ -v

# Single Python test
PYTHONPATH=starter-code pytest starter-code/tests/test_firm_analysis.py::test_compute_metrics_profit_margin -v

# R tests
Rscript -e "testthat::test_file('starter-code/tests/test_firm_analysis.R')"
```

`PYTHONPATH=starter-code` is required because `firm_analysis.py` is not in a package — tests import it directly by name.

## Architecture

```
myst.yml                  ← site config and TOC
index.md / setup.md       ← top-level pages
part2-python/             ← three-step Python improvement module
part3-r-translation/      ← three-step R translation module
part4-bonus.md            ← optional parallelization exercise
starter-code/
  firm_analysis.py        ← the intentionally-messy script participants improve
  data/firms.csv          ← synthetic firm-level financial data (firm_id, year, revenue, cost, assets)
  output/summary.csv      ← tracked output; summary_r.csv added by participants
  tests/                  ← created by participants during the lab
images/                   ← screenshots used in setup.md
custom.css                ← site styling overrides
```

The lab TOC is linear: `index → setup → part1-intro → part2-python/* → part3-r-translation/* → part4-bonus → wrap-up`. All TOC entries are declared in `myst.yml`.

## MyST Authoring Conventions

**Admonition types used in this codebase:**

| Block type | MyST syntax | Purpose |
|---|---|---|
| Participant prompts | `:::{admonition} 💬 Prompt — <title>` + `:class: tip` | Exact prompts to paste into the AI tool |
| Expected AI output | `:::{note}` | What the AI should produce |
| Checkpoints | `:::{important}` with `- [ ]` checkboxes | End-of-step verification |
| Warnings | `:::{warning}` | Common mistakes or gotchas |
| Collapsible sections | `:::{dropdown} <title>` | Optional/supplemental content |
| Tabbed content | `::::{tab-set}` + `:::{tab-item} <label>` | Claude Code vs. Copilot CLI variants |

Prompt admonitions always use `💬` emoji and follow the pattern `💬 Prompt — <action phrase>` or `💬 Prompt <N> — <action phrase>`.

**Images** live in `images/` with kebab-case names prefixed by the tool they relate to:
- `github-copilot-cli-*` for Copilot CLI screenshots
- `claude-*` or `claude-cli-*` for Claude Code screenshots

## Git Commit Style

Conventional commits throughout: `feat:`, `test:`, `chore:`. The lab instructs participants to commit after each step — commit message examples in the content serve as the convention guide.

## Starter Code Design Constraints

`starter-code/firm_analysis.py` is **intentionally flat and problematic** (no functions, hardcoded paths, `print('done')`, magic numbers). Do not "fix" it preemptively — the lab exercises are built around participants discovering and correcting these issues with AI assistance.

The expected refactored function signatures are:
- `compute_metrics(df)` → adds `profit`, `profit_margin`, `roa`, `asset_turnover` columns
- `filter_firms(df, min_revenue=1_000_000)` → filters by revenue threshold
- `summarize_by_year(df)` → groups by year, rounds to 4 decimal places

Python and R tests use **the same inline fixture** (not the CSV) so they can cross-validate the translation:

```python
# Python fixture shape
{'firm_id': ['F001','F001','F002','F002'], 'year': [2020,2021,2020,2021],
 'revenue': [2_000_000, 3_000_000, 500_000, 600_000],
 'cost':    [1_200_000, 1_800_000, 350_000, 420_000],
 'assets':  [4_000_000, 5_000_000, 800_000, 900_000]}
```

## Environment (KLC Context)

The lab runs on the Kellogg Linux Cluster via Singularity. Participants use a single mamba environment (`~/copilot_dir/envs/python-virtual-env`) with Python 3.12, R, pandas, pytest, tidyverse, and testthat. The `ai_agent_container` module wraps AI tool invocations on the cluster.

Participants maintain **two simultaneous SSH connections** to KLC:
- **Terminal A** — runs the AI CLI session (`ai_agent_container`) and stays open throughout the lab
- **Terminal B** — runs commands like `python`, `pytest`, `git`, `cat`, etc. without interrupting the AI session
