# Part 1 · Introduction: Iterative AI Collaboration

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

## The Four Pillars

Every improvement in this lab targets one of four practices that separate research scripts that work-once from pipelines that are trustworthy and reusable.

| Pillar | What it means | Why it matters on KLC |
|--------|--------------|----------------------|
| **Logging** | Use `logging`, not `print()` — with timestamps and severity levels | When a SLURM job runs overnight, log lines are the only record of what happened, what failed, and why |
| **Testing** | Isolated tests for individual functions with a fixed fixture | Tests are a contract — they let you refactor or translate to R with confidence that behavior hasn't changed |
| **Abstraction** | Named functions with clear inputs and outputs; no magic numbers | Flat scripts are hard to test and impossible to import; functions are both |
| **Automation** | No hardcoded paths — use a CLI or config instead | A pipeline you have to edit before every run is a pipeline that will be edited incorrectly |

:::{note}
**Version control** underpins all four — commit after each improvement so you can always roll back to a known-good state. The examples in this lab include a commit step after every change.
:::

:::{admonition} 🗣️ Discussion — Where do you already do this?
:class: seealso
Which of these four practices do you already use in your own research code? Which do you skip most often — and why? Have you ever been burned by the absence of one of them?
:::

---

## Tool Orientation

You give the AI context — a file, an error message, a question — and it responds with code, explanations, or suggestions. The workflow throughout this lab is the same regardless of which tool you use:

> **Open file → send prompt → copy or apply the result → run or commit → repeat**

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
