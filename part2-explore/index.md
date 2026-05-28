# Part 2 · Explore and Extract

## Goal

In this part, you start from **nothing but a directory of raw SEC filings** and use AI to build a working data pipeline from scratch.

Most data analysis projects in research begin this way: you have a dataset you've never seen before, no code, and a research question. The AI coding assistant is most powerful when you treat it as a thinking partner for that exploration — not just a code generator.

By the end of Part 2, you will have:

- a working mental model of EDGAR Form 4 data and its structure
- a documented list of data quirks to watch out for
- a complete Python extraction script (`edgar_analysis.py`) that you built step by step

## Why "Look Before You Code"

When you skip straight to writing a parser, you make assumptions. Those assumptions become bugs. The EDGAR data in particular has several non-obvious quirks that will silently corrupt your output if you don't know about them.

This section teaches the habit of **asking the AI to read and describe data before asking it to write code for that data**.

## The Three Steps

| Step | What you do | What you produce |
|------|-------------|-----------------|
| [Step 1 – Understand the data](step1-understand-data.md) | Read raw files with AI, understand Form 4 structure | A mental model + proposed column schema |
| [Step 2 – Discover the quirks](step2-discover-quirks.md) | Ask AI to probe for edge cases and failure modes | A documented list of gotchas |
| [Step 3 – Build the extractor](step3-build-extractor.md) | 5 iterative prompts, each adding one capability | `starter-code/edgar_analysis.py` |

## Starting State

```text
/kellogg/data/EDGAR/4/2003/    ← 324,000 raw SEC filing text files
starter-code/                  ← empty (no Python code yet)
```

## Ending State

```text
starter-code/
├── edgar_analysis.py          ← built step-by-step in Step 3
└── output/
    └── insider_summary.csv    ← written by your script
```

:::{note}
**If you're short on time or want to skip directly to code quality work:** a pre-built version of `edgar_analysis.py` is already in the repo. You can skip to [Part 3 · Improve the Python](../part2-python/index.md) and treat it as your starting point.

That said, building it yourself in Part 2 gives you a much deeper understanding of both the data and the iterative AI workflow. We recommend starting here if this is your first time working with EDGAR data.
:::

---

**Start with [Step 1 – Understand the Data](step1-understand-data.md) →**
