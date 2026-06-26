# Bonus · Parallelization

:::{note}
This section is optional and designed for participants who finish the Improve example early, or as a take-home exercise.
:::

## The Scenario

You now have a clean, tested, configurable Python pipeline. Right now it processes 500 files sequentially. The full `/kellogg/data/EDGAR/4/2003` directory contains **324,000 files**.

Running the pipeline across all of 2003 — let alone multiple years — will take a while. The bottleneck is `parse_filing()`, which must open, read, and parse XML from each file.

The question: **can AI help you add multiprocessing without breaking your tests?**

The answer is yes — and you can use the tests to verify it immediately.

---

## Your Prompt

:::{admonition} 💬 Prompt — Add multiprocessing to the file parsing loop
:class: tip
```
I want to parallelize the parse_filing step in starter-code/edgar_analysis.py
using Python's multiprocessing module.

Please:
1. Add a --workers argument (default: 1) that controls the number of processes
2. When workers > 1, use multiprocessing.Pool to call parse_filing() on
   each file path in parallel, then flatten the results into a single list
3. Keep single-process behavior unchanged when --workers 1
4. Make sure all existing tests still pass (they test the functions
   in isolation, so parallelization is transparent to them)

Explain the approach before making the change.
```
:::

:::{note}
The AI will typically:

1. Import `multiprocessing` and add `--workers` to the argparse section
2. Replace the `for fname in files` loop with `Pool.map(parse_filing, file_paths)` when workers > 1
3. Flatten the list-of-lists result with `itertools.chain.from_iterable` or a list comprehension

The key insight: because `parse_filing`, `filter_transactions`, and `summarize_by_month` are **pure functions**, the parallelization is a wrapper around them — the functions themselves don't change, so the tests don't need to change either.
:::

---

## Run the Tests After the Change

```bash
PYTHONPATH=starter-code pytest starter-code/tests/ -v
```

All tests should still pass. The parallelization is transparent to the function-level tests.

---

## Benchmark It

```bash
time python starter-code/edgar_analysis.py --workers 1 --n-files 2000
time python starter-code/edgar_analysis.py --workers 4 --n-files 2000
```

:::{warning}
On small batches, parallelization is often *slower* — the overhead of spawning processes exceeds the parsing time. Use at least `--n-files 2000` to see a meaningful comparison. The speedup becomes significant when processing tens of thousands of files.
:::

---

## Commit

```bash
git add starter-code/edgar_analysis.py
git commit -m "feat: add optional multiprocessing with --workers argument"
```

---

**Next: [Wrap-Up](wrap-up.md) →**
