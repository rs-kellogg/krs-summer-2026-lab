# Part 1 · Introduction: Iterative AI Collaboration

## The One Rule

> **Don't ask for everything at once.**

When people first use AI coding tools, they often try one giant prompt: *"Rewrite this script into a robust, well-tested, well-logged, modular Python and R pipeline with a CLI and perfect XML parsing."*

The AI will produce something. It may even look polished. But it will be hard to trust, hard to debug, and hard to learn from.

Instead, this lab practices a different workflow:

1. **Start with working code** (even if messy)
2. **Ask the AI one thing at a time** — understand it, improve it, test it
3. **Verify each step** before moving to the next
4. **Build up trust incrementally**

This is much closer to how experienced developers actually work with AI tools.

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

:::{tab-item} Claude Code CLI
Claude Code works as a full interactive agent. Start it in your project directory:

```bash
# From the project root
claude

# Or give it an initial task
claude "read starter-code/edgar_analysis.py and explain what it does"
```

Claude Code can read, edit, and create files directly — ask it to make changes and it will do so.
:::

:::{tab-item} GitHub Copilot CLI
The most natural way to use Copilot CLI for this lab is to open an interactive session:

```bash
# Start an interactive session (recommended for this lab)
gh copilot chat
```

In interactive mode, you can paste code, ask follow-up questions, and iterate.
:::

::::

:::{admonition} 💬 Prompt — Explain the EDGAR script
:class: tip
Open your AI tool and try this first prompt:

```
Read starter-code/edgar_analysis.py and give me a brief explanation of:
1. What SEC EDGAR Form 4 filings are
2. What this script extracts from them
3. What output file it produces
4. Any obvious code quality issues you notice, without fixing them yet
```
:::

:::{note}
A good answer should explain that Form 4 filings disclose insider transactions such as open-market purchases (`P`) and sales (`S`), and that the script:

- reads SEC filing text files from `/kellogg/data/EDGAR/4/2003`
- extracts the embedded `<ownershipDocument>` XML
- pulls issuer and reporting-owner metadata plus non-derivative transactions
- filters to transaction codes `P` and `S`
- summarizes insider buy/sell activity by month

It should also notice problems like hardcoded paths, `print()` instead of logging, no functions, and no CLI.
:::

---

## Prompting Tips

A few habits make AI coding tools much more useful:

- **Give it the file, not just a description.** "Read `starter-code/edgar_analysis.py`" is better than "I have a script..."
- **One ask per prompt.** If you want logging **and** tests **and** refactoring, ask separately.
- **Paste errors verbatim.** Don't summarize traceback text.
- **Name the libraries you want.** "Use Python's `logging` module" is more precise than "add logging."
- **Ask it to explain before it edits.** Understanding first makes later changes easier to evaluate.

---

**Next: [Part 2 · Explore and Extract](part2-explore/index.md) →**
