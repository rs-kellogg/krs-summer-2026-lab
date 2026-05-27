# Part 2, Step 4 – Add a Command-Line Interface

## Why Hardcoded Paths Are a Problem

Right now `firm_analysis.py` has file paths baked directly into the source code:

```python
df = pd.read_csv('starter-code/data/firms.csv')
...
summary.to_csv('starter-code/output/summary.csv', index=False)
```

This means the script only works when run from one specific directory, with one specific dataset. On a cluster where you might run the same pipeline against many different input files — or hand the script to a colleague — this breaks immediately.

Python's `argparse` module solves this by letting users pass paths and parameters at the command line without touching the source.

---

## Your Prompt

:::{admonition} 💬 Prompt — Add a CLI with argparse
:class: tip
```
Add argparse command-line arguments to starter-code/firm_analysis.py so that
users can specify:
  --input PATH      Path to the input CSV (default: starter-code/data/firms.csv)
  --output PATH     Path to the output CSV (default: starter-code/output/summary.csv)
  --min-revenue N   Revenue threshold for filtering (default: 1000000)

The defaults should match the current hardcoded values so existing behavior is
unchanged. Log each argument value at the INFO level at startup.
```
:::

:::{note}
The AI should add something like this to `main()`:

```python
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Firm-level financial analysis pipeline")
    parser.add_argument("--input", default="starter-code/data/firms.csv",
                        help="Path to input CSV")
    parser.add_argument("--output", default="starter-code/output/summary.csv",
                        help="Path to output CSV")
    parser.add_argument("--min-revenue", type=float, default=1_000_000,
                        help="Minimum revenue threshold for filtering")
    return parser.parse_args()

def main():
    args = parse_args()
    logger.info(f"Input:       {args.input}")
    logger.info(f"Output:      {args.output}")
    logger.info(f"Min revenue: {args.min_revenue}")

    df = pd.read_csv(args.input)
    ...
    df = filter_firms(df, min_revenue=args.min_revenue)
    ...
    summary.to_csv(args.output, index=False)
```
:::

---

## Verify the Defaults Still Work

Running with no arguments should behave exactly as before:

```bash
python starter-code/firm_analysis.py
```

Then try it with explicit arguments:

```bash
python starter-code/firm_analysis.py \
  --input starter-code/data/firms.csv \
  --output starter-code/output/summary.csv \
  --min-revenue 2000000
```

Re-run the tests to confirm nothing broke:

```bash
PYTHONPATH=starter-code pytest starter-code/tests/ -v
```

---

## Commit

```bash
git add starter-code/firm_analysis.py
git commit -m "feat: add argparse CLI (--input, --output, --min-revenue)"
```

:::{important}
- [ ] Running with no arguments produces the same `summary.csv` as before
- [ ] `--min-revenue 2000000` produces a different (smaller) output
- [ ] All pytest tests still pass
- [ ] The change is committed to git
:::

---

**Next: [Part 3 · Python → R](../part3-r-translation/index.md) →**
