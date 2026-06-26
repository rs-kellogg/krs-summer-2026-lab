# Part 3, Step 1 – Before You Change Anything, Understand It

:::{dropdown} starter-code/edgar_analysis.py — the script you'll be improving
```python
"""
edgar_analysis.py — starter script for the AI-Assisted Research Data Lab

Parses SEC EDGAR Form 4 (insider trading) filings and produces a monthly
summary of non-derivative buy and sell transactions by corporate insiders.

Note: This is intentionally written in a flat, non-modular style with
hardcoded paths — improving it is the goal of the lab exercises.
"""

import os
import re
import xml.etree.ElementTree as ET
import pandas as pd

DATA_DIR = '/kellogg/data/EDGAR/4/2003'
OUTPUT_PATH = 'starter-code/output/insider_summary.csv'
N_FILES = 500

files = sorted(os.listdir(DATA_DIR))[:N_FILES]

records = []

for fname in files:
    fpath = os.path.join(DATA_DIR, fname)
    with open(fpath, 'r', errors='replace') as f:
        content = f.read()

    xml_match = re.search(r'<ownershipDocument>.*?</ownershipDocument>', content, re.DOTALL)
    if not xml_match:
        continue

    try:
        root = ET.fromstring(xml_match.group())
    except ET.ParseError:
        print(f'skipping {fname} — XML parse error')
        continue

    issuer = root.find('issuer')
    if issuer is None:
        continue
    issuer_name = (issuer.findtext('issuerName') or '').strip()
    issuer_cik  = (issuer.findtext('issuerCik')  or '').strip()

    owner = root.find('reportingOwner')
    if owner is None:
        continue
    owner_name  = (owner.findtext('reportingOwnerId/rptOwnerName') or '').strip()
    rel         = owner.find('reportingOwnerRelationship')
    is_director = (rel.findtext('isDirector') or '0').strip() == '1' if rel is not None else False
    is_officer  = (rel.findtext('isOfficer')  or '0').strip() == '1' if rel is not None else False

    # Handle both X0101 (nonDerivativeSecurity) and X0201 (nonDerivativeTable/nonDerivativeTransaction)
    txn_elements = root.findall('nonDerivativeTable/nonDerivativeTransaction')
    if not txn_elements:
        txn_elements = root.findall('nonDerivativeSecurity')

    for txn in txn_elements:
        txn_date   = (txn.findtext('transactionDate/value') or '').strip()
        txn_code   = (txn.findtext('transactionCoding/transactionCode') or '').strip()
        shares_str = (txn.findtext('transactionAmounts/transactionShares/value') or '').strip()
        price_str  = (txn.findtext('transactionAmounts/transactionPricePerShare/value') or '').strip()
        if not price_str:
            price_str = (txn.findtext('transactionAmounts/transactionValue/value') or '').strip()
        acq_disp   = (txn.findtext('transactionAmounts/transactionAcquiredDisposedCode/value') or '').strip()

        try:
            shares = float(shares_str)
            price  = float(price_str) if price_str else None
        except ValueError:
            continue

        records.append({
            'issuer_name':       issuer_name,
            'issuer_cik':        issuer_cik,
            'owner_name':        owner_name,
            'is_director':       is_director,
            'is_officer':        is_officer,
            'transaction_date':  txn_date,
            'transaction_code':  txn_code,
            'shares':            shares,
            'price_per_share':   price,
            'acquired_disposed': acq_disp,
        })

print(f'Extracted {len(records)} transactions from {N_FILES} files')

df = pd.DataFrame(records)
df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')
df['month'] = df['transaction_date'].dt.to_period('M').astype(str)

df = df[df['transaction_code'].isin(['P', 'S'])]
print(f'After filtering to purchases (P) and sales (S): {len(df)} rows')

summary = df.groupby(['month', 'transaction_code']).agg(
    n_transactions=('shares', 'count'),
    total_shares=('shares', 'sum'),
    mean_price=('price_per_share', 'mean'),
).reset_index()

summary = summary.round(2)
summary.to_csv(OUTPUT_PATH, index=False)
print('done')
```
:::

:::{admonition} Chat interface — paste the starter code first
:class: seealso
Before using any prompts on this page, expand the dropdown above and paste the full script into your chat conversation with a brief note: *"Here is the script I'll be working with."* Then proceed with the prompts below.
:::

## Slow Down First

A common mistake with AI tools is jumping straight to "fix this" before establishing a shared understanding of what the code does.

If you ask the AI to explain code *before* asking it to change code, you get two benefits:

1. You can catch cases where the AI misunderstands the logic
2. You build a mental model that makes later changes easier to evaluate

---

## Your Prompts

:::::{tab-set}
::::{tab-item} Chat Interface
:::{admonition} 💬 Prompt 1 — Explain the filing and the script
:class: tip
```
Using the script I just pasted, explain in plain English:

1. What an SEC EDGAR Form 4 filing is
2. What metadata this script extracts from each filing
3. How it handles the two XML schema variants (X0101 and X0201)
4. What the final CSV summary contains
```
:::
::::
::::{tab-item} CLI Tools
:::{admonition} 💬 Prompt 1 — Explain the filing and the script
:class: tip
```
Read starter-code/edgar_analysis.py and explain, in plain English:

1. What an SEC EDGAR Form 4 filing is
2. What metadata this script extracts from each filing
3. How it handles the two XML schema variants (X0101 and X0201)
4. What the final CSV summary contains
```
:::
::::
:::::

:::::{tab-set}
::::{tab-item} Chat Interface
:::{admonition} 💬 Prompt 2 — List code quality issues without fixing them
:class: tip
```
Now list the code quality issues in the script above.

Do not fix anything yet. Give me a numbered list of problems, and for each one,
explain why it matters in a research computing context (e.g., running on a
cluster, sharing with collaborators, reproducing results).
```
:::
::::
::::{tab-item} CLI Tools
:::{admonition} 💬 Prompt 2 — List code quality issues without fixing them
:class: tip
```
Now list the code quality issues in starter-code/edgar_analysis.py.

Do not fix anything yet. Give me a numbered list of problems, and for each one,
explain why it matters in a research computing context (e.g., running on a
cluster, sharing with collaborators, reproducing results).
```
:::
::::
:::::

:::{note}
A strong answer should identify most or all of these issues:

1. **Hardcoded `DATA_DIR`** — only works on KLC unless the source code is edited
2. **Hardcoded `OUTPUT_PATH`** — difficult to rerun the pipeline with a different destination
3. **Magic number `N_FILES = 500`** — unclear why 500 files are used; hard to change safely
4. **`print()` instead of logging** — no timestamps, severity levels, or persistent log file
5. **No functions / no modularity** — parsing, filtering, and summarizing are all tangled together
6. **Weak error handling** — malformed or incomplete filings can silently drop data
7. **No `argparse` CLI** — users must edit the source instead of passing parameters at runtime

That's your roadmap for Part 2.
:::

:::{admonition} 🗣️ Discussion — Have you seen these before?
:class: seealso
Of these 7 issues, which ones have you run into in your own research code — or inherited from a collaborator? Which were hardest to track down as a bug?
:::

---

## Version Control Checkpoint

Before making any changes, commit the current state so you have a clean baseline:

```bash
git add starter-code/edgar_analysis.py
git commit -m "chore: add EDGAR starter script before improvements"
```

:::{important}
- [ ] You can explain in one or two sentences what a Form 4 filing is
- [ ] You can describe what `edgar_analysis.py` extracts and summarizes
- [ ] You have a list of at least 6 code-quality issues
- [ ] You created a clean baseline git commit before editing
:::

---

**Next: [Step 2 – Add Logging](step2-logging.md) →**
