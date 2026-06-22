# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A MyST Markdown static-site lab — a 90-minute hands-on workshop teaching researchers to use AI coding assistants (GitHub Copilot CLI and Claude Code CLI) to build a Python data pipeline against real SEC EDGAR Form 4 insider-trading data, then translate it to R and add tests. The "code" participants write lives in `starter-code/`; everything else is documentation.

## Commands

```bash
# Local site preview (live reload)
myst start

# Production build (mirrors CI — required for GitHub Pages)
BASE_URL="/krs-summer-2026-lab" myst build --html
# Output: _build/html/

# Run the Python starter script
python starter-code/edgar_analysis.py

# Run all Python tests
PYTHONPATH=starter-code pytest starter-code/tests/ -v

# Run a single Python test
PYTHONPATH=starter-code pytest starter-code/tests/test_edgar_analysis.py::test_parse_filing_extracts_sale -v

# Run R tests (once participants create them)
Rscript -e "testthat::test_file('starter-code/tests/test_edgar_analysis.R')"
```

`PYTHONPATH=starter-code` is required because `edgar_analysis.py` is not in a package — tests import it directly by name.

CI (`.github/workflows/publish.yml`) builds and deploys to GitHub Pages on every push to `main`.

## Architecture

```
myst.yml                          ← site config and TOC
index.md / setup.md               ← top-level pages
part1-intro.md                    ← AI workflow principles
part2-explore/                    ← Track A: build from scratch (3 steps)
part2-python/                     ← Track B: improve inherited code (4 steps)
part3-r-translation/              ← Track B continued: Python → R (3 steps)
part4-bonus.md                    ← optional multiprocessing exercise
wrap-up.md
starter-code/
  edgar_analysis.py               ← intentionally-messy EDGAR script participants improve
  data/README.md                  ← explains EDGAR Form 4 data source
  output/insider_summary.csv      ← tracked reference output (N_FILES=500, 2003)
  tests/                          ← created by participants during the lab
images/                           ← screenshots used in setup.md
custom.css                        ← site styling overrides
```

The TOC is linear: `index → setup → part1-intro → part2-explore/* → part2-python/* → part3-r-translation/* → part4-bonus → wrap-up`. All TOC entries must be declared in `myst.yml`.

## Starter Code Design Constraints

`starter-code/edgar_analysis.py` is **intentionally flat and problematic** — no functions, hardcoded paths, `print()` calls, magic numbers. Do not "fix" it preemptively; the exercises are built around participants discovering and correcting these issues with AI assistance.

The expected refactored function signatures (from the lab exercises) are:
- `parse_filing(filepath)` → list of transaction dicts
- `filter_transactions(df, codes=['P','S'])` → filtered DataFrame
- `summarize_by_month(df)` → groups by month + transaction_code, rounds to 2 decimal places

Python and R tests use the same minimal filing fixture — a minimal `<ownershipDocument>` XML in a fake SEC-DOCUMENT envelope with one sale transaction (1000 shares at $25.50) — so they can cross-validate the translation.

`starter-code/output/insider_summary.csv` is tracked in git as the reference output and must not change unless the pipeline logic changes.

## MyST Authoring Conventions

| Block type | MyST syntax | Purpose |
|---|---|---|
| Participant prompts | `:::{admonition} 💬 Prompt — <title>` + `:class: tip` | Exact prompts to paste into the AI tool |
| Expected AI output | `:::{note}` | What the AI should produce |
| Checkpoints | `:::{important}` with `- [ ]` checkboxes | End-of-step verification |
| Warnings | `:::{warning}` | Common mistakes or gotchas |
| Collapsible sections | `:::{dropdown} <title>` | Optional/supplemental content |
| Tabbed content | `::::{tab-set}` + `:::{tab-item} <label>` | Claude Code vs. Copilot CLI variants |

Prompt admonitions always use `💬` and follow the pattern `💬 Prompt — <action phrase>` or `💬 Prompt <N> — <action phrase>`.

Images live in `images/` with kebab-case names prefixed by tool: `github-copilot-cli-*` for Copilot, `claude-*` or `claude-cli-*` for Claude Code.

## EDGAR Data

Data lives at `/kellogg/data/EDGAR/4/2003/` on KLC — ~324,000 Form 4 filing text files. Each file has an SEC-DOCUMENT header plus an embedded `<ownershipDocument>` XML block with two schema variants:
- **X0101** (older): `nonDerivativeSecurity` elements
- **X0201** (newer): `nonDerivativeTable/nonDerivativeTransaction`

The starter script processes the first 500 files (sorted alphabetically) and produces an 18-row monthly summary of P (purchase) and S (sale) transactions.

## Git Commit Style

Conventional commits throughout: `feat:`, `test:`, `chore:`, `fix:`. The lab instructs participants to commit after each step; examples in the lab content serve as the convention guide.
