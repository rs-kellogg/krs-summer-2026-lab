# Part 3 · Python → R Translation

## Goal

You now have a Python pipeline that is:

- ✅ Logged
- ✅ Tested
- ✅ Modular

Now you'll translate it to R — even if you've never written R before. The AI will do the translation; your job is to use your tests to verify the result is correct.

This is the core use case: **using AI to cross language boundaries while using tests as a safety net.**

## The Three Steps

| Step | What you ask the AI | What you get |
|------|-------------------|-------------|
| [Step 1 – Translate](step1-translate.md) | *Translate to R using tidyverse* | A working R script |
| [Step 2 – Write R tests](step2-tests.md) | *Write testthat equivalents* | R test suite — with at least one revealing failure |
| [Step 3 – Fix & refactor](step3-fix-refactor.md) | *Fix discrepancies, add CLI args* | Verified, configurable R + Python pipelines |

## Why One of the R Tests Will Fail

This is not an accident. It's the point.

AI translation is very good but not perfect. There are subtle differences between pandas and tidyverse behavior — in how ties are broken in `median()`, how grouped rounding is applied, default NA handling. A single test failure will demonstrate concretely why you never just accept a translation without validation.

---

## Starting State

```
starter-code/
├── firm_analysis.py     ← Python, refactored and tested
├── tests/
│   └── test_firm_analysis.py
└── ...
```

## Ending State

```
starter-code/
├── firm_analysis.py         ← now accepts --input, --output, --min-revenue args
├── firm_analysis.R          ← R translation, tested and verified
├── tests/
│   ├── test_firm_analysis.py
│   └── test_firm_analysis.R
└── ...
```

---

**Start with [Step 1 – Translate to R](step1-translate.md) →**
