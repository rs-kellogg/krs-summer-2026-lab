# Part 3 · Python → R Translation

## Goal

You now have a Python pipeline that is:

- ✅ logged
- ✅ tested
- ✅ modular
- ✅ configurable

Now you'll translate it to R.

This is a **Python-to-R translation exercise** using `xml2` for XML parsing, `dplyr` for data manipulation, and `readr` for CSV output. The AI will do most of the translation work; your job is to verify that the R version behaves like the Python version.

## The Three Steps

| Step | What you ask the AI | What you get |
|------|-------------------|-------------|
| [Step 1 – Translate](step1-translate.md) | *Translate the EDGAR pipeline to R* | A working R script using `xml2`, `dplyr`, and `readr` |
| [Step 2 – Write R tests](step2-tests.md) | *Mirror the Python tests with testthat* | An R test suite for parsing, filtering, and summarizing |
| [Step 3 – Compare outputs and fix divergences](step3-fix-refactor.md) | *Find and fix Python/R mismatches* | Matching Python and R monthly summaries |

## Starting State

```text
starter-code/
├── edgar_analysis.py
├── output/
│   └── insider_summary.csv
└── tests/
    └── test_edgar_analysis.py
```

## Ending State

```text
starter-code/
├── edgar_analysis.py
├── edgar_analysis.R
├── output/
│   ├── insider_summary.csv
│   └── insider_summary_r.csv
└── tests/
    ├── test_edgar_analysis.py
    └── test_edgar_analysis.R
```

The goal is not just "get an R script that runs." The goal is **make the R script agree with the tested Python behavior**.

---

**Start with [Step 1 – Translate to R](step1-translate.md) →**
