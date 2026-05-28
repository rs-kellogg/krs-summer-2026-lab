# Copilot Instructions

## What This Repository Is

A **MyST Markdown static-site lab** — a 90-minute hands-on workshop where participants use AI coding assistants (GitHub Copilot CLI and Claude Code CLI) to build a Python data pipeline from scratch against real SEC EDGAR Form 4 data, then translate it to R and add tests. The "code" participants actually write lives in `starter-code/`; the rest of the repo is documentation.

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
# Python pipeline (run from repo root)
python starter-code/edgar_analysis.py

# R pipeline (once created by lab participants)
Rscript starter-code/edgar_analysis.R
```

## Tests

```bash
# All Python tests
PYTHONPATH=starter-code pytest starter-code/tests/ -v

# Single Python test
PYTHONPATH=starter-code pytest starter-code/tests/test_edgar_analysis.py::test_parse_filing_extracts_sale -v

# R tests
Rscript -e "testthat::test_file('starter-code/tests/test_edgar_analysis.R')"
```

`PYTHONPATH=starter-code` is required because `edgar_analysis.py` is not in a package — tests import it directly by name.

## Architecture

```
myst.yml                  ← site config and TOC
index.md / setup.md       ← top-level pages
part2-python/             ← four-step Python improvement module
part3-r-translation/      ← three-step R translation module
part4-bonus.md            ← optional parallelization exercise
starter-code/
  edgar_analysis.py       ← the intentionally-messy EDGAR parsing script participants improve
  data/README.md          ← explains the EDGAR data source (live at /kellogg/data/EDGAR/4/2003/)
  output/insider_summary.csv  ← tracked reference output (N_FILES=500, 2003 only)
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

`starter-code/edgar_analysis.py` is **intentionally flat and problematic** (no functions, hardcoded paths, `print('done')`, magic numbers). Do not "fix" it preemptively — the lab exercises are built around participants discovering and correcting these issues with AI assistance.

The expected refactored function signatures are:
- `parse_filing(filepath)` → list of transaction dicts (reads file, extracts XML, parses non-derivative transactions)
- `filter_transactions(df, codes=['P','S'])` → filtered DataFrame
- `summarize_by_month(df)` → groups by month + transaction_code, rounds to 2 decimal places

Python and R tests use **the same minimal filing fixture** (not the real data files) so they can cross-validate the translation. The fixture is a minimal `<ownershipDocument>` XML embedded in a fake SEC-DOCUMENT envelope with one sale transaction (1000 shares at $25.50).

## Environment (KLC Context)

The lab runs on the Kellogg Linux Cluster via Singularity. Participants use a single mamba environment (`~/copilot_dir/envs/edgar-env`) with Python 3.12, R, pandas, pytest, xml2, tidyverse, and testthat. The `ai_agent_container` module wraps AI tool invocations on the cluster.

Participants maintain **two simultaneous SSH connections** to KLC:
- **Terminal A** — runs the AI CLI session (`ai_agent_container`) and stays open throughout the lab
- **Terminal B** — runs commands like `python`, `pytest`, `git`, `cat`, etc. without interrupting the AI session

## EDGAR Data

The data lives at `/kellogg/data/EDGAR/4/2003/` on KLC — approximately 324,000 Form 4 filing text files. Each file contains:
- An SEC-DOCUMENT header with issuer and reporting-owner metadata
- An embedded `<ownershipDocument>` XML block with transaction details
- Two schema variants: X0101 (older, `nonDerivativeSecurity` elements) and X0201 (newer, `nonDerivativeTable/nonDerivativeTransaction`)

The starter script processes the first 500 files (sorted alphabetically) and produces an 18-row monthly summary of P (purchase) and S (sale) transactions.
