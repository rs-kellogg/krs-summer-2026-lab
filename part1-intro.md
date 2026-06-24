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

:::{admonition} 🗣️ Discussion — Where do you already do this?
:class: seealso
Which of these four practices do you already use in your own research code? Which do you skip most often — and why?
:::

---

## Tool Orientation

Both tools work from your terminal. You give them context (a file, an error message, a question) and they respond with code, explanations, or suggestions.

:::{note}
**You are currently in `edgar-scratch`** — your from-scratch repo. The AI agent was started there in Setup step 8. There's no code here yet; that's the point. Your first interactions with the AI will be about *understanding* the data, not writing code.
:::

::::{tab-set}

:::{tab-item} Claude Code CLI
Claude Code works as a full interactive agent. Start it in your project directory:

```bash
# From edgar-scratch
claude

# Or give it an initial task
claude "look at 2-3 files in /kellogg/data/EDGAR/4/2003/ and tell me what kind of data this is"
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

:::{tab-item} Claude.ai Chat
Go to [claude.ai](https://claude.ai) and open a new conversation. No startup command is needed.

To establish shared context at the start of your session:

```
I'm working through a hands-on data exercise using real SEC EDGAR Form 4
insider-trading filings. I'll be pasting file contents and asking you to help
me understand the data, write Python code, and eventually translate it to R.
Please work with me one step at a time — I'll verify each step before moving on.
```
:::

::::

:::{admonition} 💬 Prompt — Explore the EDGAR data
:class: tip
Open your AI tool and try this first prompt:

```
Look at 3 files in /kellogg/data/EDGAR/4/2003/ — pick ones with different
filenames. For each file, briefly describe:
1. What format the file is in
2. What kind of information it seems to contain
3. What fields or data points look extractable

Don't write any code yet. Just describe what you see.
```
:::

:::{note}
A good answer should notice:

- The files are SEC Form 4 filings — insider trading disclosures
- Each file has a plain-text header (SEC-DOCUMENT metadata), then an embedded XML block (`<ownershipDocument>`)
- The XML contains: issuer name and CIK, reporting owner name and role (director/officer), and a table of transactions (shares, price, date, transaction code)
- Transaction codes P (purchase), S (sale), A (award/grant), and others are present
- There are variations in XML structure across files

This mental model is what you'll build on throughout Part 2.
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
