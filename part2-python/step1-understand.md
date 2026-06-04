# Part 3, Step 1 – Before You Change Anything, Understand It

## Slow Down First

A common mistake with AI tools is jumping straight to "fix this" before establishing a shared understanding of what the code does.

If you ask the AI to explain code *before* asking it to change code, you get two benefits:

1. You can catch cases where the AI misunderstands the logic
2. You build a mental model that makes later changes easier to evaluate

---

## Your Prompts

:::{admonition} 💬 Prompt 1 — Explain the filing and the script
:class: tip
```
Read starter-code/edgar_analysis.py and explain, in plain English:

1. What an SEC EDGAR Form 4 filing is
2. What metadata this script extracts from each filing
3. How it handles the two XML schema variants (X0101 and X0201)
4. What the final CSV summary contains
```
:::

:::{admonition} 💬 Prompt 2 — List code quality issues without fixing them
:class: tip
```
Now list the code quality issues in starter-code/edgar_analysis.py.

Do not fix anything yet. Give me a numbered list of problems, and for each one,
explain why it matters in a research computing context (e.g., running on a
cluster, sharing with collaborators, reproducing results).
```
:::

:::{note}
A strong answer should identify most or all of these issues:

1. **Hardcoded `DATA_DIR`** — only works on KLC unless the source code is edited
2. **Hardcoded `OUTPUT_PATH`** — difficult to rerun the pipeline with a different destination
3. **Magic number `N_FILES = 500`** — unclear why 500 files are used; hard to change safely
4. **`print()` instead of logging** — no timestamps, severity levels, or persistent log file
5. **No functions / no modularity** — parsing, filtering, and summarizing are all tangled together
6. **Weak error handling** — malformed or incomplete filings can silently drop data
7. **No `argparse` CLI** — users must edit the source instead of passing parameters at runtime

That's your roadmap for Part 2.
:::

---

## Version Control Checkpoint

Before making any changes, commit the current state so you have a clean baseline:

```bash
git add starter-code/edgar_analysis.py
git commit -m "chore: add EDGAR starter script before improvements"
```

:::{important}
- [ ] You can explain in one or two sentences what a Form 4 filing is
- [ ] You can describe what `edgar_analysis.py` extracts and summarizes
- [ ] You have a list of at least 6 code-quality issues
- [ ] You created a clean baseline git commit before editing
:::

---

**Next: [Step 2 – Add Logging](step2-logging.md) →**
