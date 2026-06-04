# AI-Assisted Research Data Lab

**Using Copilot CLI & Claude Code to build better research pipelines**

## About This Lab

This is a **90-minute hands-on lab** where you will use AI coding assistants — [GitHub Copilot CLI](https://githubnext.com/projects/copilot-cli) and [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) — to develop and improve a data analysis pipeline.

The central idea: **AI tools are most powerful when used interactively and iteratively**, not when you dump all your requirements into a single prompt and hope for the best.

By the end of this lab, you will have practiced using AI to:

- 📋 **Add structured logging** so you know what your pipeline is doing on a remote cluster
- 🧪 **Write unit tests** that verify your code is correct — and catch bugs introduced by translation
- 🔄 **Translate Python to R** (or vice versa) with confidence, using tests as a safety net
- 🧱 **Refactor hardcoded scripts** into modular, configurable pipelines

---

## Two Tracks, One Lab

This lab covers two complementary skills. You'll work through both in sequence, using separate git repositories so each has its own history.

::::{grid} 2

:::{grid-item-card} 🔬 Track A · Build from Scratch
**Repo: `edgar-scratch`** (starts empty)

Parts 2 · Explore and Extract

You have raw EDGAR data and no code. You use AI as a thinking partner to understand the data, discover its quirks, and build a working pipeline iteratively — one prompt, one working step at a time.
:::

:::{grid-item-card} 🛠 Track B · Improve Inherited Code
**Repo: `edgar-improve`** (pre-loaded starter script)

Parts 3 · Improve Python, 4 · Python → R

You inherit a working-but-messy script. You use AI to add logging, write unit tests, refactor into functions, add a CLI, and translate to R.
:::

::::

---

## What You'll Build

You start with **two repos**:

- **`edgar-scratch`** — completely empty
- **`edgar-improve`** — contains this working but messy Python script:

```python
# edgar_analysis.py  (your starting point — it works, but...)
import os
import re
import xml.etree.ElementTree as ET
import pandas as pd

DATA_DIR = '/kellogg/data/EDGAR/4/2003'
OUTPUT_PATH = 'starter-code/output/insider_summary.csv'
N_FILES = 500

files = sorted(os.listdir(DATA_DIR))[:N_FILES]

records = []

# ... parse filings, extract transactions, summarize by month ...

summary.to_csv(OUTPUT_PATH, index=False)
print('done')
```

You end up with:

- **`edgar-scratch`**: a complete extraction pipeline you wrote from scratch, built step by step with AI guidance
- **`edgar-improve`**: **two well-tested, well-logged, modular, configurable pipelines — one in Python, one in R — that parse EDGAR insider trading data and summarize buy/sell activity.**

---

## Lab Timeline

| Time | Section | Repo |
|------|---------|------|
| 0:00 – 0:10 | [Setup & Orientation](setup.md) | *(setup)* |
| 0:10 – 0:25 | [Part 1 · Introduction](part1-intro.md) | `edgar-scratch` |
| 0:25 – 0:55 | [Part 2 · Explore and Extract](part2-explore/index.md) | `edgar-scratch` |
| 0:55 – 1:15 | [Part 3 · Improve the Python](part2-python/index.md) | `edgar-improve` ← switch here |
| 1:15 – 1:30 | [Part 4 · Python → R](part3-r-translation/index.md) *(or take-home)* | `edgar-improve` |
| *(optional)* | [Bonus · Parallelization](part4-bonus.md) | `edgar-improve` |
| last 5 min | [Wrap-Up](wrap-up.md) | — |

---

## How to Use This Book

Each page uses the same four block types:

:::{admonition} 💬 Prompt — Try this in your AI tool
:class: tip
These are the exact prompts to paste into Copilot CLI or Claude Code.
:::

:::{note}
These explain what the AI should produce and what to look for.
:::

:::{important}
- [ ] These are your checkpoints for each step.
:::

:::{warning}
These flag common mistakes, gotchas, and things to verify before moving on.
:::

This lab is designed to be followed **step by step**. Don't skip straight to "make it perfect." Ask the AI to help with one improvement at a time, run the code, inspect the results, and commit each meaningful change.

---

**Ready? Start with [Setup](setup.md) →**
