# Part 2, Step 2 – Discover the Quirks Before You Build

## Find the Surprises Early

When you parse thousands of real-world files, bugs usually come from the cases you didn't anticipate. The best time to find edge cases is *before* you write the parser — not after it silently drops 20% of your data.

This step systematically probes the EDGAR data for structural variation and failure modes. It takes 10–15 minutes. It will save you significant debugging time in Step 3.

---

:::{dropdown} Sample filing data — for chat interface users
**Sample Filing 3** — X0201 schema, `nonDerivativeTable` (compare with Sample Filing 1 from Step 1)

```text
-----BEGIN PRIVACY-ENHANCED MESSAGE-----

<SEC-DOCUMENT>
<SEC-HEADER>
CONFORMED SUBMISSION TYPE:	4
FILED AS OF DATE:		20030901
ISSUER:
	COMPANY DATA:
		CONFORMED NAME:		ACME CORP
		CENTRAL INDEX KEY:	0001100200
REPORTING-OWNER:
	OWNER DATA:
		COMPANY CONFORMED NAME:	SMITH JANE A
		CENTRAL INDEX KEY:	0001100201
</SEC-HEADER>
<DOCUMENT>
<TEXT>
<XML>
<ownershipDocument>
    <schemaVersion>X0201</schemaVersion>
    <issuer>
        <issuerCik>0001100200</issuerCik>
        <issuerName>ACME CORP</issuerName>
    </issuer>
    <reportingOwner>
        <reportingOwnerId>
            <rptOwnerCik>0001100201</rptOwnerCik>
            <rptOwnerName>SMITH JANE A</rptOwnerName>
        </reportingOwnerId>
        <reportingOwnerRelationship>
            <isDirector>0</isDirector>
            <isOfficer>1</isOfficer>
            <officerTitle>Chief Financial Officer</officerTitle>
        </reportingOwnerRelationship>
    </reportingOwner>
    <nonDerivativeTable>
        <nonDerivativeTransaction>
            <securityTitle><value>Common Stock</value></securityTitle>
            <transactionDate><value>2003-08-15</value></transactionDate>
            <transactionCoding><transactionCode>P</transactionCode></transactionCoding>
            <transactionAmounts>
                <transactionShares><value>500</value></transactionShares>
                <transactionPricePerShare><value>12.50</value></transactionPricePerShare>
                <transactionAcquiredDisposedCode><value>A</value></transactionAcquiredDisposedCode>
            </transactionAmounts>
        </nonDerivativeTransaction>
    </nonDerivativeTable>
</ownershipDocument>
</XML>
</TEXT>
</DOCUMENT>
</SEC-DOCUMENT>
-----END PRIVACY-ENHANCED MESSAGE-----
```

**Sample Filing 4** — hard-wrapped XML (element names split across lines at ~80 characters)

```text
-----BEGIN PRIVACY-ENHANCED MESSAGE-----

<SEC-DOCUMENT>
<SEC-HEADER>
CONFORMED SUBMISSION TYPE:	4
FILED AS OF DATE:		20030612
</SEC-HEADER>
<DOCUMENT>
<TEXT>
<XML>
<ownershipDocument>    <schemaVersion>X0101</schemaVersion>    <issuer>        <issuerCi
k>0001000180</issuerCik>        <issuerName>GLOBAL INDUSTRIES LTD</issuerName>    </iss
uer>    <reportingOwner>        <reportingOwnerId>            <rptOwnerCik>000108142</rp
tOwnerCik>            <rptOwnerName>DOE JAMES E</rptOwnerName>        </reportingOwnerI
d>        <reportingOwnerRelationship>            <isDirector>1</isDirector>            
<isOfficer>0</isOfficer>        </reportingOwnerRelationship>    </reportingOwner>    <n
onDerivativeSecurity>        <securityTitle><value>Common Stock</value></securityTitle> 
       <transactionDate><value>2003-06-10</value></transactionDate>        <transactionC
oding>            <transactionCode>S</transactionCode>        </transactionCoding>      
  <transactionAmounts>            <transactionShares><value>2000</value></transactionSha
res>            <transactionValue><value>8.50</value></transactionValue>        </transa
ctionAmounts>    </nonDerivativeSecurity></ownershipDocument>
</XML>
</TEXT>
</DOCUMENT>
</SEC-DOCUMENT>
-----END PRIVACY-ENHANCED MESSAGE-----
```
:::

## Your Prompts

:::::{tab-set}
::::{tab-item} CLI Tools
:::{admonition} 💬 Prompt 1 — Sample broadly for structural variation
:class: tip
```
Look at 8–10 files in /kellogg/data/EDGAR/4/2003/, choosing files with
different issuer CIK numbers from the filenames.

Focus on the XML structure inside each file. What structural differences
do you notice between files? Are they all organized the same way?
```
:::
::::
::::{tab-item} Chat Interface
:::{admonition} 💬 Prompt 1 — Compare two XML schemas
:class: tip
Copy **Sample Filing 1** (from Step 1's dropdown) and **Sample Filing 3** (from the dropdown above). Paste both at the end of this message:

```
Here are two real SEC EDGAR Form 4 filings. Focus on the XML structure
inside each one. What structural differences do you notice? Are the
non-derivative transactions organized the same way in both files?

[paste Sample Filing 1 here]

---

[paste Sample Filing 3 here]
```
:::
::::
:::::

:::{note}
A thorough answer will discover at least two important structural differences:

**Schema version differences:**

The files contain two XML schema variants:

| Schema | XML element for stock transactions | Price field |
|--------|-----------------------------------|-------------|
| **X0101** (older) | `<nonDerivativeSecurity>` directly under root | `<transactionValue>` |
| **X0201** (newer) | `<nonDerivativeTable>/<nonDerivativeTransaction>` | `<transactionPricePerShare>` |

Both schemas have the same logical structure — they just use different element names. A robust parser needs to check for both.

**Other variations:**
- Some filings contain *only* derivative transactions (stock options, warrants) — no non-derivative transactions at all
- Some filings have a single transaction; others have dozens
- The `schemaVersion` element (`X0101` or `X0201`) is available in the XML and can be used to detect which schema applies
:::

---

:::::{tab-set}
::::{tab-item} CLI Tools
:::{admonition} 💬 Prompt 2 — Find files that break standard XML parsing
:class: tip
```
Try to parse the XML from this file using Python's xml.etree.ElementTree:
/kellogg/data/EDGAR/4/2003/1000180_3_0001242648-03-000002.txt

What error do you get? Look at the raw file around the error location.
Why does it fail, and what would be needed to fix it?
```
:::
::::
::::{tab-item} Chat Interface
:::{admonition} 💬 Prompt 2 — Understand the malformed XML problem
:class: tip
Copy **Sample Filing 4** from the dropdown above and paste it at the end of this message:

```
Here is a real SEC EDGAR Form 4 filing. If I tried to parse the XML
inside it using Python's xml.etree.ElementTree, what error would I
get and why? Look carefully at the structure of the XML content.
What would be needed to fix it?

[paste Sample Filing 4 here]
```
:::
::::
:::::

::::{note}
This is the most important quirk in the dataset.

**What happens:** `ET.fromstring()` raises:
```
xml.etree.ElementTree.ParseError: not well-formed (invalid token): line 21, column 0
```

**Why it fails:** The XML content in this file is written as a single very long line, then **hard-wrapped at ~120 characters** at the file level. This splits XML element names across line boundaries — for example, `</officerTitle>` becomes `</offi` at the end of one line and `cerTitle>` at the start of the next. Since a tag name cannot contain a newline, this is invalid XML.

**The fix:**

```python
xml_match = re.search(r'<ownershipDocument>.*?</ownershipDocument>', content, re.DOTALL)
xml_str = xml_match.group().replace('\n', ' ')   # ← join the wrapped lines
root = ET.fromstring(xml_str)
```

Removing newlines from the extracted XML block before parsing recovers data from these files.

**Scale:** About 20% of files in this dataset have this issue. Without the fix, you silently lose roughly 1 in 5 filings.

:::{warning}
The starter script (`edgar_analysis.py`) in the repo uses the simpler approach — it just skips files that fail to parse. That's a deliberate design choice for readability.

If you want to recover those ~20% of filings, add `.replace('\n', ' ')` before the `ET.fromstring()` call in Step 3. The tests and expected output in the repo use the "skip" approach as the baseline.
:::
::::

---

:::::{tab-set}
::::{tab-item} CLI Tools
:::{admonition} 💬 Prompt 3 — Probe for missing and zero-value fields
:class: tip
```
Look at several filings and focus on the price and shares fields inside
<transactionAmounts>.

Are these fields always populated? What values do you see for:
- transactions with code 'A' (awards/grants)
- transactions with code 'S' or 'P' (market trades)

What should our parser do when price is missing or zero?
```
:::
::::
::::{tab-item} Chat Interface
:::{admonition} 💬 Prompt 3 — Understand missing price fields
:class: tip
No file needed — send this prompt directly:

```
In SEC EDGAR Form 4 filings, the price field inside <transactionAmounts>
is not always populated. Based on what you know about Form 4 transaction types:

- When would a transaction with code 'A' (award/grant) have a missing or zero price?
- When would an 'S' or 'P' (open-market trade) have a missing price?
- What should a data parser do when the price field is blank?
```
:::
::::
:::::

:::{note}
Price fields are commonly blank or zero in:

- **Award transactions** (`code=A`): shares are granted at $0 or with no price field — the insider isn't paying market price
- **Gift and transfer transactions** (`code=J`): price is typically 0 or absent
- **Some open-market trades**: the price field is sometimes left blank even for `S` and `P` transactions, especially in older filings

Best practice: store `None` (Python) or `NaN` (pandas) for missing prices rather than dropping the record. This preserves the transaction count and share volumes even when price data is unavailable.

Your column schema from Step 1 should handle this: `price_per_share` as a nullable float.
:::

---

## Summary: Quirks to Remember

Keep this list in mind when building the extractor in Step 3:

| # | Quirk | Impact | Fix |
|---|-------|--------|-----|
| 1 | Two XML schemas: `nonDerivativeSecurity` (X0101) vs `nonDerivativeTable/nonDerivativeTransaction` (X0201) | Missing transactions if only one path is checked | Try X0201 first, fall back to X0101 |
| 2 | Price field name differs by schema: `transactionPricePerShare` (X0201) vs `transactionValue` (X0101) | Missing prices | Try `transactionPricePerShare` first, fall back to `transactionValue` |
| 3 | Hard-wrapped XML (line breaks mid-element-name) in ~20% of files | Parse errors silently drop 1 in 5 filings | Remove newlines before parsing (or skip and log) |
| 4 | Price is blank or zero for non-market transactions (awards, gifts) | Division errors or misleading averages | Store as `None`/`NaN`, not 0 |
| 5 | Some filings have only derivative (option) transactions | Empty non-derivative transaction list | Handle gracefully — just produce no rows |

---

:::{important}
- [ ] You can name both XML schema versions and what they call the price field
- [ ] You understand why ~20% of files fail to parse and what causes it
- [ ] You know to store `None` for missing prices rather than dropping records
- [ ] You have the quirk table above to reference during Step 3
:::

---

**Next: [Step 3 – Build the Extractor](step3-build-extractor.md) →**
