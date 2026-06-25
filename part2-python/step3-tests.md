# Part 3, Step 3 – Refactor and Test

## Why Refactor Before Testing?

Right now the script is one flat sequence of code. That makes it impossible to test individual steps in isolation.

The solution is to ask the AI to do two things in one controlled step:

1. **Refactor the script into named functions**
2. **Write pytest tests against those functions**

This is the key move that makes the later Python-to-R translation trustworthy. If Python tests pass, and R tests pass with the same fixture, you know the translation is correct.

---

:::{admonition} 🗣️ Discussion — What's most likely to break silently?
:class: seealso
Before writing any tests: what behavior in this script is most likely to break silently — without throwing an error or exception? What would "wrong but not crashing" look like here?
:::

---

## The Strategic Ask

:::::{tab-set}
::::{tab-item} CLI Tools
:::{admonition} 💬 Prompt — Refactor into functions and add pytest tests
:class: tip
```
I need to add unit tests to starter-code/edgar_analysis.py, but the logic is
currently in one flat script.

Please do two things:

1. Refactor the script into these three functions:
   - parse_filing(filepath) -> list of dicts
     Reads one EDGAR filing, extracts the ownershipDocument XML,
     returns a list of non-derivative transaction records.
   - filter_transactions(df, codes=['P', 'S']) -> DataFrame
     Keeps only rows whose transaction_code is in codes.
   - summarize_by_month(df) -> DataFrame
     Groups by month and transaction_code, computes n_transactions,
     total_shares, and mean_price, rounded to 2 decimal places.

2. Keep the script behavior the same when run normally:
   - still reads files from DATA_DIR
   - still filters to P and S by default
   - still writes starter-code/output/insider_summary.csv

3. Write pytest tests at starter-code/tests/test_edgar_analysis.py that test
   each function. For parse_filing(), use pytest's tmp_path fixture to write a
   minimal filing to a temporary file. For the other functions, use small
   inline DataFrames.

4. Put all execution logic in a main() function guarded by
   if __name__ == '__main__': so the script is importable.
```
:::
::::
::::{tab-item} Chat Interface
:::{admonition} 💬 Prompt — Refactor into functions and add pytest tests
:class: tip
```
I need to add unit tests to the script above, but the logic is currently
in one flat script.

Please do two things:

1. Refactor the script into these three functions:
   - parse_filing(filepath) -> list of dicts
     Reads one EDGAR filing, extracts the ownershipDocument XML,
     returns a list of non-derivative transaction records.
   - filter_transactions(df, codes=['P', 'S']) -> DataFrame
     Keeps only rows whose transaction_code is in codes.
   - summarize_by_month(df) -> DataFrame
     Groups by month and transaction_code, computes n_transactions,
     total_shares, and mean_price, rounded to 2 decimal places.

2. Keep the script behavior the same when run normally:
   - still reads files from DATA_DIR
   - still filters to P and S by default
   - still writes starter-code/output/insider_summary.csv

3. Write pytest tests at starter-code/tests/test_edgar_analysis.py that test
   each function. For parse_filing(), use pytest's tmp_path fixture to write a
   minimal filing to a temporary file. For the other functions, use small
   inline DataFrames.

4. Put all execution logic in a main() function guarded by
   if __name__ == '__main__': so the script is importable.
```
:::
::::
:::::

::::{note}
**Refactored `edgar_analysis.py`** should expose three functions:

```python
def parse_filing(filepath):
    """Read one EDGAR filing and return a list of transaction dicts."""
    ...

def filter_transactions(df, codes=['P', 'S']):
    """Keep only rows with transaction_code in codes."""
    return df[df['transaction_code'].isin(codes)].copy()

def summarize_by_month(df):
    """Group by month + transaction_code and aggregate."""
    ...
```

:::{dropdown} What test_edgar_analysis.py should look like
```python
import pandas as pd
import pytest
from edgar_analysis import parse_filing, filter_transactions, summarize_by_month

MINIMAL_FILING = """-----BEGIN PRIVACY-ENHANCED MESSAGE-----

<SEC-DOCUMENT>
<SEC-HEADER>
CONFORMED SUBMISSION TYPE: 4
</SEC-HEADER>
<DOCUMENT>
<TEXT>
<XML>
<ownershipDocument>
    <issuer>
        <issuerCik>0001000015</issuerCik>
        <issuerName>TEST CORP</issuerName>
    </issuer>
    <reportingOwner>
        <reportingOwnerId>
            <rptOwnerCik>0001234567</rptOwnerCik>
            <rptOwnerName>DOE JOHN</rptOwnerName>
        </reportingOwnerId>
        <reportingOwnerRelationship>
            <isDirector>1</isDirector>
            <isOfficer>0</isOfficer>
        </reportingOwnerRelationship>
    </reportingOwner>
    <nonDerivativeTable>
        <nonDerivativeTransaction>
            <transactionDate><value>2003-06-15</value></transactionDate>
            <transactionCoding>
                <transactionCode>S</transactionCode>
            </transactionCoding>
            <transactionAmounts>
                <transactionShares><value>1000</value></transactionShares>
                <transactionPricePerShare><value>25.50</value></transactionPricePerShare>
                <transactionAcquiredDisposedCode><value>D</value></transactionAcquiredDisposedCode>
            </transactionAmounts>
        </nonDerivativeTransaction>
    </nonDerivativeTable>
</ownershipDocument>
</XML>
</TEXT>
</DOCUMENT>
</SEC-DOCUMENT>
-----END PRIVACY-ENHANCED MESSAGE-----
"""


def test_parse_filing_extracts_sale(tmp_path):
    filing_path = tmp_path / "sample_form4.txt"
    filing_path.write_text(MINIMAL_FILING)

    records = parse_filing(filing_path)

    assert len(records) == 1
    assert records[0]['transaction_code'] == 'S'
    assert records[0]['shares'] == 1000.0
    assert records[0]['price_per_share'] == pytest.approx(25.50)


def test_filter_transactions_keeps_ps():
    df = pd.DataFrame({
        'transaction_code': ['S', 'P', 'A', 'J'],
        'shares': [100, 200, 300, 400],
        'price_per_share': [10.0, 20.0, 30.0, 40.0],
    })

    filtered = filter_transactions(df)

    assert list(filtered['transaction_code']) == ['S', 'P']


def test_summarize_by_month_counts():
    df = pd.DataFrame({
        'transaction_date': ['2003-06-01', '2003-06-15', '2003-07-02'],
        'transaction_code': ['S', 'S', 'P'],
        'shares': [100.0, 150.0, 200.0],
        'price_per_share': [10.0, 12.0, 8.0],
    })
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    df['month'] = df['transaction_date'].dt.to_period('M').astype(str)

    summary = summarize_by_month(df)

    assert len(summary) == 2

    june_s = summary[(summary['month'] == '2003-06') & (summary['transaction_code'] == 'S')]
    assert june_s['n_transactions'].iloc[0] == 2
    assert june_s['total_shares'].iloc[0] == 250.0
```
:::
::::

---

## Run the Tests

:::{important}
**Before asking the AI to run the tests**, remind it to use the Python interpreter from the conda environment you set up. This is the first time the agent will execute Python code, so it needs to know which interpreter to use.
:::

::::{tab-set}
:::{tab-item} CLI Tools
From the repo root:

```bash
PYTHONPATH=starter-code pytest starter-code/tests/ -v
```

You should see:

```
tests/test_edgar_analysis.py::test_parse_filing_extracts_sale PASSED
tests/test_edgar_analysis.py::test_filter_transactions_keeps_ps PASSED
tests/test_edgar_analysis.py::test_summarize_by_month_counts PASSED
```

Then rerun the full script to confirm behavior is unchanged:

```bash
python starter-code/edgar_analysis.py
cat starter-code/output/insider_summary.csv
```
:::
:::{tab-item} Chat Interface
Paste the generated `test_edgar_analysis.py` back into the conversation and ask:

*"Trace through `test_parse_filing_extracts_sale` step by step. What does `tmp_path` provide? What does `parse_filing` return for the MINIMAL_FILING fixture? Do all three assertions pass?"*

Then ask the same for the other two tests. This is a slower substitute for running pytest, but it builds the same mental model.
:::
::::

:::{warning}
If pytest can't import `edgar_analysis`, make sure you're using the `PYTHONPATH=starter-code` prefix or run from the `starter-code/` directory.

You can also ask the AI: *"pytest can't import edgar_analysis — how do I fix the module path?"*
:::

---

## Commit

```bash
git add starter-code/edgar_analysis.py starter-code/tests/test_edgar_analysis.py
git commit -m "feat: refactor EDGAR pipeline and add pytest tests"
```

:::{important}
- [ ] `edgar_analysis.py` now has `parse_filing()`, `filter_transactions()`, and `summarize_by_month()`
- [ ] `starter-code/tests/test_edgar_analysis.py` exists and all 3 tests pass
- [ ] Running the script still produces the same 18-row monthly summary CSV
- [ ] The change is committed to git
:::

---

**Next: [Step 4 – Add a CLI](step4-cli.md) →**
