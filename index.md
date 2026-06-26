# Kellogg Research Computing Lab

## Why This Lab Exists

Research scripts usually start simple: read some files, extract what you need, write a CSV. But as projects grow, the same patterns cause the same problems.

**Sound familiar?**

- The script runs on your laptop but breaks on the Linux cluster because the path is hardcoded
- You submitted a SLURM job overnight and woke up to `print('done')` — no timestamps, no error count, no indication of what actually ran
- You want to rerun on 2004 data but changing one value requires editing the source file
- A collaborator asks "what happens if a filing is malformed?" and the honest answer is "...it probably just skips it?"
- You translated the pipeline to R and the numbers don't quite match — and you're not sure which version is right

These are not exotic problems. They are the normal condition of research code — and they all have straightforward fixes.

**This lab gives you hands-on practice with four of them, working on real data on KLC.** AI coding assistants (Claude, GitHub Copilot) are available throughout as a resource — but the skills you're building are yours.

---

## The Four Pillars

| Pillar | The problem it solves | What you'll build |
|--------|----------------------|-------------------|
| **Logging** | "The job ran — but what actually happened?" | Replace `print()` with timestamped log lines that tell you exactly what processed, what failed, and where output went |
| **Testing** | "I changed something and I'm not sure it still works" | Write pytest tests that catch silent failures and let you refactor or translate with confidence |
| **Abstraction** | "I can't reuse this without editing the source" | Refactor flat scripts into named functions with clean inputs, outputs, and documented contracts |
| **Automation** | "Every time I run this I have to edit the file" | Add a CLI so the script is configurable at runtime — path, file count, output destination — without touching source code |

Each pillar is one focused step: one bounded change, run to verify it works, then committed to version control. AI coding assistants are available to help generate and explain code at each step — but the discipline of making one change at a time and verifying the result is the core skill.

:::{admonition} 🗣️ Discussion — Where do you already do this?
:class: seealso
Which of these four practices do you already use in your own research code? Which do you skip most often — and why? Have you ever been burned by the absence of one of them?
:::

---

## The Data

You'll work with real **SEC EDGAR Form 4** filings — insider trading disclosures that every corporate officer, director, and major shareholder must file when they buy or sell company stock.

The dataset lives on the **Kellogg Linux Cluster (KLC)** at `/kellogg/data/EDGAR/4/2003/` — about 324,000 plain-text filing files from 2003, each containing an embedded XML block with transaction details.

This is a realistic research dataset: messy, inconsistent, partially malformed, and large enough that you can't inspect every file by hand. It's exactly the kind of data where logging, testing, abstraction, and automation pay off most.

---

## The Examples

The lab is organized as self-contained examples. Work through them in order, or jump directly to the skill most relevant to your own work.

**Example: Explore the Data** — start from raw KLC data and no code; understand the dataset, discover its quirks, and build a working parser step by step.

| Step | What you do |
|------|-------------|
| [Understand the data](part2-explore/step1-understand-data.md) | Read raw files with AI — don't write code yet |
| [Discover the quirks](part2-explore/step2-discover-quirks.md) | Find schema variants, malformed files, missing fields before building |
| [Build the extractor](part2-explore/step3-build-extractor.md) | Five incremental prompts, each adding one capability |

**Example: Improve a Script** — take a working-but-messy inherited script and apply all four pillars, one focused step at a time.

| Step | Pillar | What you do |
|------|--------|-------------|
| [Understand the starter code](part2-python/step1-understand.md) | — | Read and critique before changing anything |
| [Add logging](part2-python/step2-logging.md) | **Logging** | Replace `print()` with structured log output |
| [Add tests](part2-python/step3-tests.md) | **Testing** + **Abstraction** | Refactor into functions, write pytest tests |
| [Add a CLI](part2-python/step4-cli.md) | **Automation** | Make the script configurable at runtime |

**Bonus**

| | |
|---|---|
| [Translate to R](part3-r-translation/index.md) | Port the Python pipeline to R; use tests to verify the two implementations agree |
| [Parallelization](part4-bonus.md) | Speed up the pipeline with multiprocessing |

---

## How to Use This Book

Each page uses four block types:

:::{admonition} 💬 Prompt — Try this in your AI tool
:class: tip
These are the exact prompts to paste into your AI tool.
:::

:::{note}
These explain what the AI should produce and what to look for.
:::

:::{important}
- [ ] These are your checkpoints — verify before moving on.
:::

:::{warning}
These flag common mistakes and gotchas.
:::

Prompts appear in two tabs: **Chat Interface** (claude.ai or similar — open in a browser tab alongside your text editor) and **CLI Tools** (Claude Code or GitHub Copilot CLI running on KLC). The chat tab is shown first; pick whichever matches your setup.

---

**Ready? Start with [Setup](setup.md) →**
