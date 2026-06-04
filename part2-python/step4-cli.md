# Part 3, Step 4 – Add a CLI

## Why a CLI Matters

Right now the script only works with one baked-in dataset, one output path, and one file limit.

That is fine for a starter exercise, but not for a reusable research pipeline. A command-line interface lets you rerun the same code against different years, subsets, or output paths without editing the source file — which is exactly what you need on a cluster where you might run the same pipeline across many different directories.

---

## Your Prompt

:::{admonition} 💬 Prompt — Add argparse command-line arguments
:class: tip
```
Add argparse to starter-code/edgar_analysis.py so the script accepts:

  --data-dir PATH   Path to the directory of EDGAR filing text files
                    (default: /kellogg/data/EDGAR/4/2003)
  --output PATH     Path to the output CSV
                    (default: starter-code/output/insider_summary.csv)
  --n-files N       Number of files to process (default: 500, type=int)

Requirements:
- Keep the defaults equal to the current hardcoded values
- Preserve existing behavior when the script is run with no arguments
- Use the CLI values inside main()
- Log the chosen values at INFO level at startup
```
:::

:::{note}
A typical implementation adds a `parse_args()` function and replaces the hardcoded constants with `args.data_dir`, `args.output`, and `args.n_files`:

```python
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Summarize insider buy/sell transactions from EDGAR Form 4 filings"
    )
    parser.add_argument("--data-dir", default="/kellogg/data/EDGAR/4/2003",
                        help="Directory containing EDGAR filing text files")
    parser.add_argument("--output", default="starter-code/output/insider_summary.csv",
                        help="Path to output CSV")
    parser.add_argument("--n-files", type=int, default=500,
                        help="Maximum number of files to process")
    return parser.parse_args()
```

At startup, you'd see log lines like:

```
INFO Data directory: /kellogg/data/EDGAR/4/2003
INFO Output:         starter-code/output/insider_summary.csv
INFO File limit:     500
```
:::

---

## Verify the Defaults

First, run with no arguments — behavior should be identical to before:

```bash
python starter-code/edgar_analysis.py
cat starter-code/output/insider_summary.csv
```

With the defaults (`--n-files 500`), you should get this 18-row summary:

```text
month,transaction_code,n_transactions,total_shares,mean_price
2003-01,P,1,4008030.0,
2003-04,P,2,0.0,0.0
2003-04,S,1,100.0,5.0
2003-05,P,12,44383.0,10.27
2003-05,S,29,260159.0,27.67
2003-06,P,7,5683.0,14.32
2003-06,S,47,606940.0,15.37
2003-07,P,10,11250.0,6.03
2003-07,S,10,46300.0,4.32
2003-08,P,35,699566.0,4.65
2003-08,S,6,30200.0,23.9
2003-09,P,7,7547.0,12.97
2003-09,S,39,259050.0,3.17
2003-10,P,1,43000.0,6.54
2003-10,S,22,50698.0,4.73
2003-11,P,14,31555.0,17.77
2003-11,S,45,201885.0,51.7
2003-12,S,37,570720.0,19.8
```

Try overriding individual arguments:

```bash
# Process only 100 files
python starter-code/edgar_analysis.py --n-files 100

# Write to a different output file
python starter-code/edgar_analysis.py --output /tmp/test_output.csv
```

Re-run the tests to confirm nothing broke:

```bash
PYTHONPATH=starter-code pytest starter-code/tests/ -v
```

---

## Commit

```bash
git add starter-code/edgar_analysis.py
git commit -m "feat: add argparse CLI to EDGAR pipeline"
```

:::{important}
- [ ] The script accepts `--data-dir`, `--output`, and `--n-files`
- [ ] Running with no arguments produces the same 18-row summary as before
- [ ] `--n-files 100` produces a shorter output (fewer transactions)
- [ ] All pytest tests still pass
:::

---

**Next: [Part 4 · Python → R](../part3-r-translation/index.md) →**
