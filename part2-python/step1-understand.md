# Part 2, Step 1 – Understand the Code

## Before You Change Anything, Understand It

A common mistake with AI tools is jumping straight to "fix this" before establishing a shared understanding of what the code does. This step deliberately slows you down.

If you ask the AI to explain code *before* asking it to change code, you get two benefits:

1. You can catch cases where the AI misunderstands the logic (and correct it before it makes bad edits)
2. You build a mental model that makes the AI's later changes easier to evaluate

---

## Your Prompts

:::{admonition} 💬 Prompt 1 — Explain the script
:class: tip
```
Read starter-code/firm_analysis.py and give me a plain-English explanation of:
1. What data it reads and what each column means
2. What calculations it performs (step by step)
3. What the output file contains
```
:::

Read the response carefully. Does it match your understanding?

:::{admonition} 💬 Prompt 2 — Identify problems (without fixing them)
:class: tip
```
Now list the code quality issues in firm_analysis.py. Do not fix anything yet —
just give me a numbered list of problems, and for each one, explain why it's
a problem in a research computing context (e.g., running on a cluster,
collaborating with others, reproducing results).
```
:::

:::{note}
The AI should identify most or all of these:

1. **Hardcoded file paths** — breaks when run from a different directory or by a different person
2. **`print('done')` instead of logging** — provides no useful diagnostic information
3. **No functions** — the entire script is one flat sequence; nothing is reusable or testable in isolation
4. **Magic number `1000000`** — unclear what this threshold represents or where it came from
5. **No error handling** — if the CSV is missing or malformed, you get an unhelpful traceback
6. **No docstrings or comments** — future-you (or a collaborator) won't know why decisions were made

You don't need to agree with every item on the list. The point is to have a concrete roadmap.
:::

---

## Version Control Checkpoint

Before making any changes, commit the current state so you have a clean baseline to compare against:

```bash
git add starter-code/firm_analysis.py
git commit -m "chore: add starter script before improvements"
```

:::{important}
- [ ] You can describe in one sentence what `firm_analysis.py` does
- [ ] You have a list of at least 4 issues the AI identified
- [ ] You have a clean git commit with the unmodified script
:::

---

**Next: [Step 2 – Add Logging](step2-logging.md) →**
