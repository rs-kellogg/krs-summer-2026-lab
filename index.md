# AI-Assisted Data Analysis Lab

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

You start with this — a working but messy Python script that analyzes firm-level financial data:

```python
# firm_analysis.py  (your starting point — it works, but...)
import pandas as pd

df = pd.read_csv('starter-code/data/firms.csv')
df['profit'] = df['revenue'] - df['cost']
df['profit_margin'] = df['profit'] / df['revenue']
df['roa'] = df['profit'] / df['assets']
df['asset_turnover'] = df['revenue'] / df['assets']
df = df[df['revenue'] > 1000000]
summary = df.groupby('year').agg(
    n_firms=('firm_id', 'count'),
    mean_profit_margin=('profit_margin', 'mean'),
    median_profit_margin=('profit_margin', 'median'),
    mean_roa=('roa', 'mean'),
    mean_asset_turnover=('asset_turnover', 'mean')
).reset_index()
summary = summary.round(4)
summary.to_csv('starter-code/output/summary.csv', index=False)
print('done')
```

You end up with **two well-tested, well-logged, modular, configurable pipelines** — one in Python, one in R — that produce identical output.

---

## Lab Timeline

| Time | Section |
|------|---------|
| 0:00 – 0:10 | [Setup & Orientation](setup.md) |
| 0:10 – 0:25 | [Part 1 · Introduction](part1-intro.md) |
| 0:25 – 0:45 | [Part 2 · Improve the Python](part2-python/index.md) |
| 0:45 – 1:10 | [Part 3 · Python → R](part3-r-translation/index.md) |
| 1:10 – 1:25 | [Bonus · Parallelization](part4-bonus.md) *(optional)* |
| 1:25 – 1:30 | [Wrap-Up](wrap-up.md) |

---

## How to Use This Book

Each page has four kinds of blocks:

:::{admonition} 💬 Your Prompt
:class: tip
These are the exact prompts to paste into Copilot CLI or Claude Code.
:::

:::{note}
These explain what the AI will produce and what to look for.
:::

:::{important}
**✅ Checkpoint** — these tell you what you should have at this point.
:::

:::{warning}
**⚠️ Watch Out** — these flag common mistakes or things that can go wrong.
:::

---

**Ready? Start with [Setup](setup.md) →**
