# Part 1 · Introduction: Iterative AI Collaboration

## The One Rule

> **Don't ask for everything at once.**

When people first use AI coding tools, they try to write one enormous prompt: *"Write me a well-tested, well-logged, modular Python script that reads firm data, computes financial metrics, filters it, summarizes by year, and accepts command-line arguments."*

The AI will produce something. It will look plausible. And it will be hard to trust, hard to debug, and hard to learn from.

Instead, this lab practices a different workflow:

1. **Start with working code** (even if messy)
2. **Ask the AI one thing at a time** — understand it, improve it, test it
3. **Verify each step** before moving to the next
4. **Build up trust incrementally**

This is closer to how experienced developers actually work with AI tools.

---

## The Four Principles

Throughout this lab, we'll use AI to reach four goals:

| Principle | What it means | Why it matters |
|-----------|--------------|----------------|
| **Verbose logging** | Use a proper logging framework, not `print()` | On a compute cluster, you need to know what ran, when, and why it failed |
| **Unit tests** | Isolated tests for individual functions | Tests are a *contract* — they let you refactor or translate code with confidence |
| **Version control** | Commit each meaningful change | You can always roll back, and you have a record of what changed |
| **Modular / configurable** | No hardcoded paths or magic numbers | Code you can reuse without editing the source |

---

## Tool Orientation

Both tools work from your terminal. You give them context (a file, an error message, a question) and they respond with code, explanations, or suggestions.

::::{tab-set}

:::{tab-item} GitHub Copilot CLI
The most natural way to use Copilot CLI for this lab is the `suggest` and `explain` commands, or by opening an interactive session:

```bash
# Ask a question about a file
gh copilot suggest -t shell "add logging to firm_analysis.py"

# Or start an interactive session (recommended for this lab)
gh copilot chat
```

In interactive mode, you can paste code, ask follow-up questions, and iterate.
:::

:::{tab-item} Claude Code CLI
Claude Code works as a full interactive agent. Start it in your project directory:

```bash
# From the project root
claude

# Or give it an initial task
claude "look at starter-code/firm_analysis.py and tell me what it does"
```

Claude Code can read, edit, and create files directly — ask it to make changes and it will do so.
:::

::::

:::{admonition} 💬 Warm-Up Prompt
:class: tip
Open your AI tool and try this first prompt to orient it to the project:

```
I have a Python script at starter-code/firm_analysis.py that analyzes firm-level
financial data. Please read it and give me a brief (3-4 sentence) description of
what it does, and list any code quality issues you notice without fixing them yet.
```
:::

:::{note}
The AI will describe the script's logic (load CSV → compute metrics → filter → summarize → save) and likely flag:

- Hardcoded file paths
- No logging (just `print('done')`)
- No functions / no modularity
- No input validation or error handling
- No tests

Hold on to this list — we're going to address each item one at a time.
:::

---

## Prompting Tips

Before we dive in, a few habits that make AI coding tools more useful:

- **Give it the file, not a description of the file.** "Read `firm_analysis.py`" is better than "I have a script that..."
- **One ask per prompt.** If you want logging AND tests AND refactoring, ask for them separately.
- **Paste error messages verbatim.** Don't summarize them.
- **Tell it the language/library you want.** "Using Python's `logging` module" is more precise than "add logging."
- **Ask it to explain before it edits.** "What would you change and why?" before "Make the change."

---

**Next: [Part 2 · Improve the Python](part2-python/index.md) →**
