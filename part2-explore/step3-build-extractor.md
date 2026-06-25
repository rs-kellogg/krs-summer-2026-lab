# Part 2, Step 3 – Build the Extractor, One Step at a Time

:::{admonition} Chat interface — how to use this step
:class: seealso
The five prompts below are for generating code. They work as-is in a chat interface — just send each prompt and copy the code you receive.

For the **"Run it and verify"** sections: if you have Python installed locally, save the generated code to `edgar_analysis.py` and run it. If not, ask the AI to trace through the code and predict the output — look for a "Chat interface" note after each run section.

For **git commits**: save your working code to a local file after each step instead.
:::

## One Prompt, One Working Step

You now know what the data looks like and where the edge cases are. Time to write code.

The discipline: **one prompt, one working step, then run and verify**. Don't ask the AI to produce the complete pipeline in one shot. Build it in stages, confirming that each stage actually works before moving on. This is what makes AI-assisted coding trustworthy.

You'll make five prompts. Each one builds directly on the output of the last.

---

## Prompt 1 — Read one file and print the basics

:::{admonition} 💬 Prompt 1 — Read a single filing
:class: tip
```
Write a Python script that:
1. Reads /kellogg/data/EDGAR/4/2003/1000015_2_0001233883-03-000002.txt
2. Finds the <ownershipDocument>...</ownershipDocument> XML block using
   a regular expression with re.DOTALL
3. Parses it with xml.etree.ElementTree
4. Prints: the issuer name, reporting owner name, whether they are a
   director, and whether they are an officer

Save the script as starter-code/edgar_analysis.py
```
:::

:::{note}
The script should look roughly like this:

```python
import re
import xml.etree.ElementTree as ET

filepath = '/kellogg/data/EDGAR/4/2003/1000015_2_0001233883-03-000002.txt'

with open(filepath, 'r', errors='replace') as f:
    content = f.read()

xml_match = re.search(r'<ownershipDocument>.*?</ownershipDocument>', content, re.DOTALL)
root = ET.fromstring(xml_match.group())

issuer_name = root.findtext('issuer/issuerName', '').strip()
owner_name  = root.findtext('reportingOwner/reportingOwnerId/rptOwnerName', '').strip()
rel         = root.find('reportingOwner/reportingOwnerRelationship')
is_director = rel.findtext('isDirector', '0') == '1' if rel is not None else False
is_officer  = rel.findtext('isOfficer',  '0') == '1' if rel is not None else False

print(f'Issuer:   {issuer_name}')
print(f'Owner:    {owner_name}')
print(f'Director: {is_director}')
print(f'Officer:  {is_officer}')
```
:::

::::{tab-set}
:::{tab-item} CLI Tools
Run it and verify:

```bash
python starter-code/edgar_analysis.py
```

Expected output:
```
Issuer:   META GROUP INC
Owner:    RUBIN HOWARD A
Director: True
Officer:  True
```
:::
:::{tab-item} Chat Interface
Ask: *"Based on this code, what would it print when run on a file with issuer META GROUP INC and owner RUBIN HOWARD A who is both a director and officer?"*
:::
::::

If you have Python locally, run it and verify. Then commit (or save to file):

```bash
git add starter-code/edgar_analysis.py
git commit -m "chore: initial single-file EDGAR reader"
```

---

## Prompt 2 — Extract the transactions

:::{admonition} 💬 Prompt 2 — Extract non-derivative transactions
:class: tip
```
Extend starter-code/edgar_analysis.py to also extract and print all
non-derivative (stock) transactions from the same file.

For each transaction, print on one line:
  date | code | shares | price

The file uses the older X0101 schema where non-derivative transactions
are <nonDerivativeSecurity> elements and price is in <transactionValue>.
Handle the case where price is missing or blank.
```
:::

:::{note}
The transaction extraction loop should look like:

```python
for txn in root.findall('nonDerivativeSecurity'):
    date      = txn.findtext('transactionDate/value', '').strip()
    code      = txn.findtext('transactionCoding/transactionCode', '').strip()
    shares    = txn.findtext('transactionAmounts/transactionShares/value', '').strip()
    price     = txn.findtext('transactionAmounts/transactionValue/value', '').strip()
    price_out = price if price else 'N/A'
    print(f'{date} | {code} | {shares} | {price_out}')
```

Now is a good time to ask the AI about the schema difference:

*"If a file used the newer X0201 schema, the transactions would be under `nonDerivativeTable/nonDerivativeTransaction` and the price would be in `transactionPricePerShare`. How should we handle both schemas in the same script?"*

The AI should suggest checking for X0201 first, then falling back to X0101 — which is exactly what the final script does.
:::

::::{tab-set}
:::{tab-item} CLI Tools
Run it:

```bash
python starter-code/edgar_analysis.py
```

Expected output — 5 stock sales by Howard Rubin:
```
2003-06-09 | S | 3100 | 3.8
2003-06-09 | S | 3500 | 4
2003-06-09 | S | 2500 | 3.75
2003-06-09 | S | 1900 | 3.76
2003-06-09 | S | 2500 | 3.78
```
:::
:::{tab-item} Chat Interface
Ask: *"Given this code, trace through what it would print for a `nonDerivativeSecurity` element with code S, 3100 shares, and price 3.8."*
:::
::::

Commit (or save to file):

```bash
git add starter-code/edgar_analysis.py
git commit -m "feat: extract non-derivative transactions from single filing"
```

---

## Prompt 3 — Scale to many files, track errors

:::{admonition} 💬 Prompt 3 — Process 50 files
:class: tip
```
Modify starter-code/edgar_analysis.py to process the first 50 files in
/kellogg/data/EDGAR/4/2003/ (sorted alphabetically).

Requirements:
- Loop over all 50 files
- Handle both XML schema variants (X0101 and X0201)
- Handle files that fail to parse: catch ET.ParseError and skip them
- Handle files where the <ownershipDocument> XML block is not found
- Collect all transactions into a list of dicts
- At the end, print: files processed, files skipped, transactions extracted
```
:::

:::{note}
This is where the quirks from Step 2 start to matter. The script should now:

1. Try X0201 path first: `root.findall('nonDerivativeTable/nonDerivativeTransaction')`
2. Fall back to X0101: `root.findall('nonDerivativeSecurity')`
3. Try `transactionPricePerShare` first, then `transactionValue`

Expected output (approximate — exact numbers depend on the first 50 files):
```
Processed: 50 files
Skipped:   11 files (XML parse errors or missing XML block)
Transactions extracted: 42
```

The skip rate (~20%) matches what we discovered in Step 2. Those are the hard-wrapped XML files.

**Ask the AI to explain the errors:**

*"About 20% of files are failing with XML parse errors. From Step 2, we know this is caused by XML content being hard-wrapped at 120 characters, splitting element names across lines. Can you show me the fix?"*

The fix:
```python
xml_str = xml_match.group().replace('\n', ' ')
root = ET.fromstring(xml_str)
```

Try implementing it. You should see the skip rate drop significantly. Whether you include this fix in the final script is your choice — the reference version in the repo skips those files, but recovering them is a good improvement to make in Part 3.
:::

:::{admonition} Chat interface — verify without running
:class: seealso
Ask: *"Trace through the error handling logic in this code. What happens when `re.search` finds no XML block? What happens when `ET.fromstring` raises a `ParseError`? Does the loop continue or crash?"*
:::

::::{tab-set}
:::{tab-item} CLI Tools
Run and verify the counts:

```bash
python starter-code/edgar_analysis.py
```
:::
:::{tab-item} Chat Interface
Ask: *"Trace through the error handling logic in this code. What happens when `re.search` finds no XML block? What happens when `ET.fromstring` raises a `ParseError`? Does the loop continue or crash?"*
:::
::::

Commit (or save to file):

```bash
git add starter-code/edgar_analysis.py
git commit -m "feat: process multiple EDGAR filings, handle parse errors"
```

---

## Prompt 4 — Build a DataFrame with a month column

:::{admonition} 💬 Prompt 4 — Convert to pandas DataFrame
:class: tip
```
Modify starter-code/edgar_analysis.py so that instead of printing each
transaction, it collects all records in a list of dicts and converts
them to a pandas DataFrame at the end.

Add these columns:
- transaction_date: convert from string to datetime using
  pd.to_datetime(errors='coerce')
- month: format as 'YYYY-MM' string derived from transaction_date

Print the DataFrame shape and first 5 rows, then print the value_counts
of transaction_code to see what types of transactions we have.

Set N_FILES = 50 as a variable at the top of the script for now.
```
:::

:::{note}
After this step you should see something like:

```
Shape: (42, 10)
   issuer_name  issuer_cik  owner_name  is_director  is_officer transaction_date transaction_code  shares  price_per_share acquired_disposed     month
0  META GROUP INC  0001000015  RUBIN HOWARD A  True  True  2003-06-09  S  3100.0  3.80  D  2003-06
...

transaction_code
S    28
A    10
P     4
dtype: int64
```

Notice that `S` (sales) are the most common non-derivative transactions — more insiders are selling than buying. This is typical for 2003, which was the beginning of a market recovery after the dot-com bust.
:::

:::{admonition} Chat interface — verify without running
:class: seealso
Ask: *"After this code runs, what columns will the DataFrame have? What will `transaction_code` value_counts look like — which codes would you expect to be most common in 2003 insider trading data?"*
:::

::::{tab-set}
:::{tab-item} CLI Tools
Run and verify:

```bash
python starter-code/edgar_analysis.py
```
:::
:::{tab-item} Chat Interface
Ask: *"After this code runs, what columns will the DataFrame have? What will `transaction_code` value_counts look like — which codes would you expect to be most common in 2003 insider trading data?"*
:::
::::

Commit (or save to file):

```bash
git add starter-code/edgar_analysis.py
git commit -m "feat: build DataFrame with month column from EDGAR transactions"
```

---

## Prompt 5 — Filter, summarize, and save to CSV

:::{admonition} 💬 Prompt 5 — Build the final summary
:class: tip
```
Add the final analysis to starter-code/edgar_analysis.py:

1. Filter the DataFrame to only purchases (P) and sales (S)
   (skip awards, gifts, and other non-market transactions)

2. Group by month and transaction_code, computing:
   - n_transactions: count of transactions
   - total_shares: sum of shares
   - mean_price: mean of price_per_share

3. Round to 2 decimal places

4. Save to starter-code/output/insider_summary.csv

5. Replace the intermediate print statements with a clean summary:
   - "Extracted N transactions from N_FILES files"
   - "After filtering to P/S: N rows"
   - "Summary written to OUTPUT_PATH (N rows)"

Also change N_FILES from 50 to 500 at the top.
```
:::

:::{note}
The key pandas operations:

```python
df = df[df['transaction_code'].isin(['P', 'S'])]

summary = df.groupby(['month', 'transaction_code']).agg(
    n_transactions=('shares', 'count'),
    total_shares=('shares', 'sum'),
    mean_price=('price_per_share', 'mean'),
).reset_index()

summary = summary.round(2)
summary.to_csv(OUTPUT_PATH, index=False)
```

Add hardcoded variables at the top:
```python
DATA_DIR    = '/kellogg/data/EDGAR/4/2003'
OUTPUT_PATH = 'starter-code/output/insider_summary.csv'
N_FILES     = 500
```
:::

Run the final script and inspect the output:

```bash
python starter-code/edgar_analysis.py
cat starter-code/output/insider_summary.csv
```

You should see 18 rows of monthly insider buy/sell data for 2003:

```text
month,transaction_code,n_transactions,total_shares,mean_price
2003-01,P,1,4008030.0,
2003-04,P,2,0.0,0.0
2003-04,S,1,100.0,5.0
2003-05,P,12,44383.0,10.27
2003-05,S,29,260159.0,27.67
...
2003-12,S,37,570720.0,19.8
```

Notice the pattern: more sells than buys in most months, especially in Q4 as the market recovered from the 2001–2002 downturn.

:::{admonition} Chat interface — verify without running
:class: seealso
Ask: *"What will the output CSV look like? How many rows should there be if we processed 500 files from 2003? What would the month and transaction_code columns contain?"*

The reference output has 18 rows — monthly P and S totals across Jan–Dec 2003.
:::

::::{tab-set}
:::{tab-item} CLI Tools
Run the final script and inspect the output:

```bash
python starter-code/edgar_analysis.py
cat starter-code/output/insider_summary.csv
```
:::
:::{tab-item} Chat Interface
Ask: *"What will the output CSV look like? How many rows should there be if we processed 500 files from 2003? What would the month and transaction_code columns contain?"*

The reference output has 18 rows — monthly P and S totals across Jan–Dec 2003.
:::
::::

Commit (or save your completed script):

```bash
git add starter-code/edgar_analysis.py starter-code/output/
git commit -m "feat: build EDGAR extractor pipeline from scratch"
```

---

## What You Just Did

In five prompts you built a complete data extraction pipeline from raw SEC filings:

1. **Read one file** — understood the structure
2. **Extracted transactions** — implemented the column schema from Step 1
3. **Scaled to many files** — handled both XML schemas and parse errors
4. **Built a DataFrame** — added time dimension with month column
5. **Filtered and summarized** — produced a research-ready CSV

Notice what made this possible:

- **You understood the data structure before coding** (Step 1) — no guessing at XML paths
- **You found the quirks before they became bugs** (Step 2) — you knew about dual schemas and wrapped XML before writing the parser
- **You built incrementally** — each prompt had a clear, verifiable output before you moved on

The script works. But look at it now: hardcoded paths, `print()` instead of logging, no functions, no CLI, no tests. Those are the exact issues you'll fix in Part 3.

---

:::{important}
- [ ] `starter-code/edgar_analysis.py` exists and runs without errors
- [ ] Running it produces `starter-code/output/insider_summary.csv` with 18 rows
- [ ] The script handles both XML schema variants (X0101 and X0201)
- [ ] Parse errors are handled without crashing
- [ ] You have at least 3 git commits showing the incremental build
:::

---

**Next: [Part 3 · Improve the Python](../part2-python/index.md) →**
