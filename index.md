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

## What You'll Build

You start with this — a working but messy Python script that parses real SEC EDGAR Form 4 filings:

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

You end up with **two well-tested, well-logged, modular, configurable pipelines — one in Python, one in R — that parse EDGAR insider trading data and summarize buy/sell activity.**

---

## Lab Timeline

| Time | Section |
|------|---------|
| 0:00 – 0:10 | [Setup & Orientation](setup.md) |
| 0:10 – 0:25 | [Part 1 · Introduction](part1-intro.md) |
| 0:25 – 0:55 | [Part 2 · Explore and Extract](part2-explore/index.md) |
| 0:55 – 1:15 | [Part 3 · Improve the Python](part2-python/index.md) |
| 1:15 – 1:30 | [Part 4 · Python → R](part3-r-translation/index.md) *(or take-home)* |
| *(optional)* | [Bonus · Parallelization](part4-bonus.md) |
| last 5 min | [Wrap-Up](wrap-up.md) |

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
