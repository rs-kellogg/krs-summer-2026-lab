# Example: Explore the Data

## What You're Doing and Why

You start from nothing but a directory of raw SEC filings and use AI to build a working data pipeline from scratch.

Most research data projects begin this way: you have a dataset you've never seen before, no code, and a research question. The first instinct is often to start writing a parser immediately — but that means making assumptions before you know what the data actually contains. Those assumptions become bugs.

This example teaches a different habit: **ask the AI to read and describe the data before writing a single line of code.** Then probe it for edge cases. Then build incrementally, one working step at a time.

By the end, you will have:

- a working mental model of EDGAR Form 4 data, its structure, and its quirks
- a complete Python extraction script you built step by step, understanding every piece

## The Three Steps

| Step | What you do | What you produce |
|------|-------------|-----------------|
| [Step 1 – Understand the data](step1-understand-data.md) | Read raw files with AI — no code yet | A mental model of Form 4 structure and fields |
| [Step 2 – Discover the quirks](step2-discover-quirks.md) | Probe for edge cases, schema variants, and failure modes | A clear picture of what will break a naive parser |
| [Step 3 – Build the extractor](step3-build-extractor.md) | Five incremental prompts, each adding one capability | A complete `starter-code/edgar_analysis.py` |

:::{note}
**Jumping directly to this example?** Chat interface users will find sample EDGAR filing data embedded in each step — no KLC access needed. CLI users should start with an empty repo (`edgar-scratch`) and the data at `/kellogg/data/EDGAR/4/2003/` on KLC.

**Want to skip to the code quality examples?** A pre-built version of `edgar_analysis.py` is the starting point for [Example: Improve a Script](../part2-python/index.md). You can go there directly — though building it yourself here gives you a deeper understanding of both the data and the iterative AI workflow.
:::

---

**Start with [Step 1 – Understand the Data](step1-understand-data.md) →**
