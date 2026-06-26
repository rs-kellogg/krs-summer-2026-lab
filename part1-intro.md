# Introduction: Building Trustworthy Research Code

## The Workflow

The examples in this lab follow the same five-step sequence. Understanding it up front helps you see why each exercise is structured the way it is.

| Step | What you do | Where in the lab |
|------|-------------|-----------------|
| **1. Read** | Ask the AI to describe the raw data — format, structure, fields. Don't write any code yet. | Example: Explore, Steps 1–2 |
| **2. Discover** | Sample broadly. Find the edge cases: schema variants, malformed files, missing values. Before you design a parser, know what will break it. | Example: Explore, Step 2 |
| **3. Build** | Write the pipeline one working step at a time. Run it. Verify the output. Then the next step. | Example: Explore, Step 3 |
| **4. Improve** | Add the practices that make code production-ready: logging, tests, a CLI. | Example: Improve, Steps 1–4 |
| **5. Translate** | Port to another language and confirm the two implementations agree on the same data. | Bonus: Translate to R |

---

## The One Rule

> **One change at a time. Run it. Verify it. Then commit.**

The most common mistake when improving a script — with or without AI — is trying to fix everything at once: add logging, refactor into functions, write tests, add a CLI, all in one pass.

The result is a script that may look better but is harder to trust, harder to debug, and harder to learn from. If something breaks, you don't know which change caused it.

Instead, this lab practices a different discipline:

1. **Start with working code** (even if messy)
2. **Make one improvement at a time** — understand it, apply it, verify it
3. **Run the script and confirm behavior is unchanged** before moving on
4. **Commit each change** so you always have a known-good state to return to

AI coding assistants — Claude, GitHub Copilot — are useful at every step for generating code, explaining unfamiliar patterns, and catching mistakes. But they work best when your asks are focused and you verify the result yourself before moving on.

:::{note}
**Version control** is what makes this discipline work. Each example in this lab ends with a commit. If a later step breaks something, you always have a known-good state to return to — and a clear record of what changed.
:::

---

## AI Coding Assistants

AI coding assistants are available throughout this lab as a resource. Use them to generate boilerplate, explain unfamiliar library APIs, debug error messages, or ask "why does this work?" — anything that accelerates the task at hand.

The core workflow is the same regardless of which tool you use:

> **Open file → make the change (with or without AI help) → run or commit → repeat**

::::{tab-set}

:::{tab-item} Claude.ai Chat
Go to [claude.ai](https://claude.ai) and open a new conversation alongside a text editor and (if on KLC) a terminal window.

To establish shared context at the start of your session:

```
I'm working through a hands-on data exercise using real SEC EDGAR Form 4
insider-trading filings. I'll be pasting file contents and asking you to help
me understand the data, write Python code, and eventually translate it to R.
Please work with me one step at a time — I'll verify each step before moving on.
```

The chat tab comes first throughout this lab — prompts are written for this workflow by default.
:::

:::{tab-item} Claude Code CLI
Claude Code works as a full interactive agent running directly on KLC. Start it in your project directory:

```bash
# From your repo directory on KLC
claude

# Or give it an initial task
claude "look at 2-3 files in /kellogg/data/EDGAR/4/2003/ and tell me what kind of data this is"
```

Claude Code can read, edit, and create files directly — ask it to make changes and it will do so without copy-pasting.
:::

:::{tab-item} GitHub Copilot CLI
Start an interactive session on KLC:

```bash
gh copilot chat
```

In interactive mode, you can paste code, ask follow-up questions, and iterate.
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

This mental model is what you'll build on throughout the Explore example.
:::

---

## Getting the Most Out of AI Assistants

A few habits make AI tools more effective when you use them:

- **Give it the file, not just a description.** "Read `starter-code/edgar_analysis.py`" is better than "I have a script..."
- **One ask per prompt.** If you want logging **and** tests **and** refactoring, ask separately — the same discipline as doing one change at a time.
- **Paste errors verbatim.** Don't summarize traceback text.
- **Name the libraries you want.** "Use Python's `logging` module" is more precise than "add logging."
- **Ask it to explain before it edits.** Understanding the change first makes it much easier to verify the result.

---

**Next: [Example: Explore the Data](part2-explore/index.md) →**
