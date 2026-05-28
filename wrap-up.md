# Wrap-Up & Key Takeaways

## What You Built

Starting from a working-but-messy Python script, you used iterative AI interaction to produce:

| Artifact | What it demonstrates |
|----------|---------------------|
| `edgar_analysis.py` (improved) | Logging, modularity, CLI arguments |
| `tests/test_edgar_analysis.py` | Unit tests as a ground-truth contract |
| `edgar_analysis.R` | AI-assisted language translation |
| `tests/test_edgar_analysis.R` | Cross-language validation |
| Git history with 5+ commits | Incremental version control |

---

## The Four Principles — Achieved

:::{note}
**📋 Verbose logging**

Replace `print()` with `logging.basicConfig()` in Python and `message()` / a logging package in R. Log file counts, parse errors, row counts, and output paths at INFO level.

**Cluster rule of thumb:** every SLURM job should produce a log file you can inspect if the job fails.
:::

:::{note}
**🧪 Unit tests**

Refactor logic into pure functions, then test them with small inline fixtures — a minimal filing XML for the parser, inline DataFrames for the filter and summarize functions. Tests are not just about catching bugs — they are a **specification** that lets you change implementation (translate, parallelize, optimize) with confidence.

**Cross-language rule of thumb:** use identical test fixtures in both languages. If both test suites pass, the translation is verified.
:::

:::{note}
**🔄 Version control**

Commit each meaningful change with a descriptive message. Use the conventional commits style: `feat:`, `test:`, `chore:`, `fix:`. Your git log should tell the story of how the code improved.

**Collaboration rule of thumb:** if you can't explain what changed between two commits from the log message alone, the commit is too vague.
:::

:::{note}
**🧱 Modular & configurable**

Extract logic into named functions. Replace hardcoded paths and magic numbers with CLI arguments and named defaults. Code you can run with `--help` and understand without reading the source is code you can reuse.

**Reusability rule of thumb:** if running your script on a colleague's machine requires editing the source file, it's not configurable enough.
:::

---

## Prompting Patterns Reference

| Pattern | When to use it | Example phrasing |
|---------|---------------|-----------------|
| **Explain first** | Before asking for changes | *"Describe what this function does before changing it"* |
| **Critique without fixing** | To get a roadmap before diving in | *"List the issues. Do not fix them yet."* |
| **One ask** | Whenever tempted to bundle multiple requests | One prompt → one change → one commit |
| **Constrain the output** | When you want a specific library or style | *"Use Python's logging module, not loguru"* |
| **Admit your level** | When working in an unfamiliar language | *"I'm not familiar with R — explain non-obvious syntax"* |
| **Paste the error** | When something fails | Paste the full traceback verbatim |
| **Ask why before fix** | When a test fails | *"What is causing this discrepancy?"* before *"Fix it"* |

---

## What to Do When AI Output Is Wrong

1. **Run it** — most AI errors are runtime errors, not logical errors. Run the code.
2. **Run the tests** — if you have tests, a failure will tell you exactly what's wrong.
3. **Paste the error back** — give the AI the full error message and ask for a fix.
4. **Narrow the scope** — if the AI keeps getting it wrong, isolate the failing function.
5. **Ask for an explanation** — *"Walk me through what this function is doing step by step."* Errors often become obvious.
6. **Trust your tests, not your eyes** — two CSVs that look the same can differ in the 4th decimal place.

---

## Further Resources

- [GitHub Copilot CLI](https://githubnext.com/projects/copilot-cli) — getting started guide
- [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code) — getting started guide
- [pytest documentation](https://docs.pytest.org/) — writing Python tests
- [testthat documentation](https://testthat.r-lib.org/) — writing R tests
- [SEC EDGAR full-text search](https://efts.sec.gov/LATEST/search-index?q=%22form+4%22) — explore the raw filings
- [Kellogg Research Computing](https://rs-kellogg.github.io/krs-public-docs-prototype/) — cluster access and datasets

---

## Your Git Log Should Look Like This

```
git log --oneline

a3f1c2e feat: add optional multiprocessing with --workers argument
b7d9e4a feat: align R EDGAR pipeline with Python output
c2a8f01 test: add R testthat suite for EDGAR pipeline
d4e3b77 feat: add initial R translation of EDGAR pipeline
e6f5c22 feat: add argparse CLI to EDGAR pipeline
f8a7d33 feat: refactor EDGAR pipeline and add pytest tests
g1b2c44 feat: replace print with structured logging
h0c3d55 chore: add EDGAR starter script before improvements
```

---

*Lab materials developed by Kellogg Research Support. Questions? Open an issue on the [GitHub repository](https://github.com/rs-kellogg/krs-summer-2026-lab).*
