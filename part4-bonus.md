# Bonus · Parallelization

:::{note}
This section is optional and designed for participants who finish Part 3 early, or as a take-home exercise.
:::

## The Scenario

You now have a clean, tested, configurable Python pipeline. Imagine the dataset is 100x larger — instead of 50 firms over 5 years, it's 5,000 firms over 20 years. The `compute_metrics()` call is fast, but suppose the bottleneck is a more expensive calculation per firm (e.g., running a regression for each firm-year).

The question: **can AI help you add multiprocessing without breaking your tests?**

The answer is yes — and you can use the tests to verify it immediately.

---

## Your Prompt

:::{admonition} 💬 Prompt — Add multiprocessing
:class: tip
```
I want to parallelize the compute_metrics step in starter-code/firm_analysis.py
using Python's multiprocessing module.

Please:
1. Add a --workers argument (default: 1) that controls the number of processes
2. When workers > 1, split the DataFrame by year and process each year's data
   in parallel using multiprocessing.Pool
3. Reassemble the results and continue with the existing filter and summarize steps
4. Make sure all existing tests still pass (they should, since they test the
   functions in isolation)

Explain the approach before making changes.
```
:::

:::{note}
The AI will typically:

1. Import `multiprocessing` and add a `--workers` argument to the argparse section
2. Wrap `compute_metrics` to handle a subset of the DataFrame
3. Use `Pool.map()` to process year-chunks in parallel
4. Concatenate the results with `pd.concat()`

The key insight: because `compute_metrics`, `filter_firms`, and `summarize_by_year` are **pure functions**, the parallelization is a wrapper around them — the functions themselves don't change, so the tests don't need to change either.
:::

---

## Run the Tests After the Change

```bash
PYTHONPATH=starter-code pytest starter-code/tests/test_firm_analysis.py -v
```

All tests should still pass. The parallelization is transparent to the function-level tests.

---

## Benchmark It

```bash
time python starter-code/firm_analysis.py --workers 1
time python starter-code/firm_analysis.py --workers 4
```

:::{warning}
On small data, parallelization is slower — the overhead of spawning processes exceeds the compute time for 250 rows. This is expected. If you want to see the speedup, ask the AI to generate a larger synthetic dataset (50,000+ rows).
:::

---

## Commit

```bash
git add starter-code/firm_analysis.py
git commit -m "feat: add optional multiprocessing with --workers argument"
```

---

**Next: [Wrap-Up](wrap-up.md) →**
