# Part 2, Step 1 – Understand the Data Before You Write Any Code

## Start by Reading, Not Coding

Before writing a single line of Python, you need to understand what you're parsing. If you hand the AI a data file and ask it to "write a parser," it will produce something. But without a shared mental model of the data, you won't be able to evaluate whether the output is correct.

The right first move: **ask the AI to read the data and explain it to you**.

AI coding assistants are excellent at this. Give one a raw file and ask what it sees — you'll get a clearer picture in two minutes than you would from spending twenty minutes reading the documentation.

---

:::{dropdown} Sample filing data — for chat interface users
**Sample Filing 1** — X0101 schema, five open-market sales (use for Prompts 1 and 3)

```text
-----BEGIN PRIVACY-ENHANCED MESSAGE-----

<SEC-DOCUMENT>
<SEC-HEADER>
ACCESSION NUMBER:		0001233883-03-000002
CONFORMED SUBMISSION TYPE:	4
FILED AS OF DATE:		20030613
ISSUER:
	COMPANY DATA:
		CONFORMED NAME:			META GROUP INC
		CENTRAL INDEX KEY:		0001000015
REPORTING-OWNER:
	OWNER DATA:
		COMPANY CONFORMED NAME:	RUBIN HOWARD A
		CENTRAL INDEX KEY:	0000912093
</SEC-HEADER>
<DOCUMENT>
<TEXT>
<XML>
<ownershipDocument>
    <schemaVersion>X0101</schemaVersion>
    <issuer>
        <issuerCik>0001000015</issuerCik>
        <issuerName>META GROUP INC</issuerName>
        <issuerTradingSymbol>METG</issuerTradingSymbol>
    </issuer>
    <reportingOwner>
        <reportingOwnerId>
            <rptOwnerCik>0000912093</rptOwnerCik>
            <rptOwnerName>RUBIN HOWARD A</rptOwnerName>
        </reportingOwnerId>
        <reportingOwnerRelationship>
            <isDirector>1</isDirector>
            <isOfficer>1</isOfficer>
            <officerTitle>Exec VP</officerTitle>
        </reportingOwnerRelationship>
    </reportingOwner>
    <nonDerivativeSecurity>
        <securityTitle><value>Common Stock</value></securityTitle>
        <transactionDate><value>2003-06-09</value></transactionDate>
        <transactionCoding><transactionCode>S</transactionCode></transactionCoding>
        <transactionAmounts>
            <transactionShares><value>3100</value></transactionShares>
            <transactionValue><value>3.8</value></transactionValue>
            <transactionAcquiredDisposedCode><value>D</value></transactionAcquiredDisposedCode>
        </transactionAmounts>
    </nonDerivativeSecurity>
    <nonDerivativeSecurity>
        <securityTitle><value>Common Stock</value></securityTitle>
        <transactionDate><value>2003-06-09</value></transactionDate>
        <transactionCoding><transactionCode>S</transactionCode></transactionCoding>
        <transactionAmounts>
            <transactionShares><value>3500</value></transactionShares>
            <transactionValue><value>4</value></transactionValue>
            <transactionAcquiredDisposedCode><value>D</value></transactionAcquiredDisposedCode>
        </transactionAmounts>
    </nonDerivativeSecurity>
    <nonDerivativeSecurity>
        <securityTitle><value>Common Stock</value></securityTitle>
        <transactionDate><value>2003-06-09</value></transactionDate>
        <transactionCoding><transactionCode>S</transactionCode></transactionCoding>
        <transactionAmounts>
            <transactionShares><value>2500</value></transactionShares>
            <transactionValue><value>3.75</value></transactionValue>
            <transactionAcquiredDisposedCode><value>D</value></transactionAcquiredDisposedCode>
        </transactionAmounts>
    </nonDerivativeSecurity>
    <nonDerivativeSecurity>
        <securityTitle><value>Common Stock</value></securityTitle>
        <transactionDate><value>2003-06-09</value></transactionDate>
        <transactionCoding><transactionCode>S</transactionCode></transactionCoding>
        <transactionAmounts>
            <transactionShares><value>1900</value></transactionShares>
            <transactionValue><value>3.76</value></transactionValue>
            <transactionAcquiredDisposedCode><value>D</value></transactionAcquiredDisposedCode>
        </transactionAmounts>
    </nonDerivativeSecurity>
    <nonDerivativeSecurity>
        <securityTitle><value>Common Stock</value></securityTitle>
        <transactionDate><value>2003-06-09</value></transactionDate>
        <transactionCoding><transactionCode>S</transactionCode></transactionCoding>
        <transactionAmounts>
            <transactionShares><value>2500</value></transactionShares>
            <transactionValue><value>3.78</value></transactionValue>
            <transactionAcquiredDisposedCode><value>D</value></transactionAcquiredDisposedCode>
        </transactionAmounts>
    </nonDerivativeSecurity>
</ownershipDocument>
</XML>
</TEXT>
</DOCUMENT>
</SEC-DOCUMENT>
-----END PRIVACY-ENHANCED MESSAGE-----
```

**Sample Filing 2** — derivative transaction only (use for Prompt 2)

```text
-----BEGIN PRIVACY-ENHANCED MESSAGE-----

<SEC-DOCUMENT>
<SEC-HEADER>
ACCESSION NUMBER:		0001259692-03-000016
CONFORMED SUBMISSION TYPE:	4
FILED AS OF DATE:		20030801
ISSUER:
	COMPANY DATA:
		CONFORMED NAME:			META GROUP INC
		CENTRAL INDEX KEY:		0001000015
REPORTING-OWNER:
	OWNER DATA:
		COMPANY CONFORMED NAME:	SALDUTTI FRANCIS J
		CENTRAL INDEX KEY:	0001259692
</SEC-HEADER>
<DOCUMENT>
<TEXT>
<XML>
<ownershipDocument>
    <schemaVersion>X0201</schemaVersion>
    <issuer>
        <issuerCik>0001000015</issuerCik>
        <issuerName>META GROUP INC</issuerName>
    </issuer>
    <reportingOwner>
        <reportingOwnerId>
            <rptOwnerCik>0001259692</rptOwnerCik>
            <rptOwnerName>SALDUTTI FRANCIS J</rptOwnerName>
        </reportingOwnerId>
        <reportingOwnerRelationship>
            <isDirector>1</isDirector>
            <isOfficer>0</isOfficer>
        </reportingOwnerRelationship>
    </reportingOwner>
    <derivativeTable>
        <derivativeTransaction>
            <securityTitle><value>Non-Qualified Stock Option</value></securityTitle>
            <conversionOrExercisePrice><value>5.90</value></conversionOrExercisePrice>
            <transactionDate><value>2003-07-28</value></transactionDate>
            <transactionCoding><transactionCode>A</transactionCode></transactionCoding>
            <transactionAmounts>
                <transactionShares><value>7500</value></transactionShares>
                <transactionAcquiredDisposedCode><value>A</value></transactionAcquiredDisposedCode>
            </transactionAmounts>
            <expirationDate><value>2013-07-28</value></expirationDate>
        </derivativeTransaction>
    </derivativeTable>
</ownershipDocument>
</XML>
</TEXT>
</DOCUMENT>
</SEC-DOCUMENT>
-----END PRIVACY-ENHANCED MESSAGE-----
```
:::

## Your Prompts

::::{tab-set}
:::{tab-item} CLI Tools
💬 **Prompt 1 — Describe a single Form 4 filing**

```
Read the file /kellogg/data/EDGAR/4/2003/1000015_2_0001233883-03-000002.txt
and explain to me:

1. What kind of document this is and why it's filed with the SEC
2. Who filed it and who it's about
3. What transaction(s) are reported and what they tell us about the insider's activity
4. The overall structure of the file — what are the major sections?
```
:::
:::{tab-item} Chat Interface
💬 **Prompt 1 — Describe a single Form 4 filing**

Copy **Sample Filing 1** from the dropdown above and paste it at the end of this message:

```
Here is a real SEC EDGAR Form 4 filing. Please explain:

1. What kind of document this is and why it's filed with the SEC
2. Who filed it and who it's about
3. What transaction(s) are reported and what they tell us about the insider's activity
4. The overall structure of the file — what are the major sections?

[paste Sample Filing 1 here]
```
:::
::::

:::{note}
A good response will explain that:

- **Form 4** is an SEC filing required whenever a corporate insider (director, officer, or >10% shareholder) buys or sells company stock — it's an insider trading disclosure
- **Issuer**: META GROUP INC, a technology research firm (SIC 8700) incorporated in Delaware
- **Reporting owner**: Howard A. Rubin, an Executive Vice President & director
- **Transactions**: 5 open-market sales of Common Stock on 2003-06-09, totaling 13,500 shares at prices ranging from $3.75 to $4.00 per share
- **Structure**: the file has two parts — a plain-text header with filing metadata, followed by a `<DOCUMENT>` section containing `<TEXT><XML>` with the actual `<ownershipDocument>` data

The transactions are "Disposed" (code `D`) and type `S` (open-market sale) — the insider is selling shares, not receiving them.
:::

---

::::{tab-set}
:::{tab-item} CLI Tools
💬 **Prompt 2 — Compare with a different filing type**

```
Now read /kellogg/data/EDGAR/4/2003/1000015_4_0001259692-03-000016.txt

How does this differ from the previous file? What type of transaction
is being reported, and what does it mean?
```
:::
:::{tab-item} Chat Interface
💬 **Prompt 2 — Compare with a different filing type**

Copy **Sample Filing 2** from the dropdown above and paste it at the end of this message:

```
Here is a second Form 4 filing from the same company. How does this
differ from the first filing? What type of transaction is being
reported, and what does it mean?

[paste Sample Filing 2 here]
```
:::
::::

:::{note}
A good response will identify key differences:

- **Different insider**: Francis J. Saldutti, a director (not an officer)
- **Different transaction type**: a **derivative** transaction — specifically, a Non-Qualified Stock Option grant for 7,500 shares, exercise price $5.90, expiring 2013
- **Different XML element**: the transaction is inside `<derivativeTable>/<derivativeTransaction>`, not `<nonDerivativeSecurity>` or `<nonDerivativeTable>/<nonDerivativeTransaction>`
- **Meaning**: the company is *granting* the director an option to buy shares in the future, not reporting an open-market trade

This is an important distinction: Form 4 covers both **direct stock transactions** (non-derivative) and **derivative instruments** like options and warrants. For research on insider *trading*, we usually care about the non-derivative transactions — the ones where the insider is actually buying or selling stock on the open market.
:::

---

:::{admonition} 💬 Prompt 3 — Design the column schema
:class: tip
```
Based on these two files, help me design the columns for a flat table
(like a spreadsheet) that captures the most research-relevant information
from a Form 4 filing.

Requirements:
- One row should represent one transaction
- Include fields from both the issuer and the reporting owner
- Focus on non-derivative (stock) transactions for now
- Note which fields might be missing or blank in some filings
```
:::

:::{note}
A reasonable schema looks like this:

| Column | Source | Notes |
|--------|--------|-------|
| `issuer_name` | Header / XML | Company name |
| `issuer_cik` | XML `<issuerCik>` | Unique company identifier |
| `owner_name` | XML `<rptOwnerName>` | Insider's name |
| `is_director` | XML `<isDirector>` | Boolean |
| `is_officer` | XML `<isOfficer>` | Boolean |
| `transaction_date` | XML `<transactionDate><value>` | YYYY-MM-DD string |
| `transaction_code` | XML `<transactionCode>` | P=purchase, S=sale, A=award, J=other |
| `shares` | XML `<transactionShares><value>` | Float; sometimes 0 |
| `price_per_share` | XML `<transactionPricePerShare>` or `<transactionValue>` | Float; sometimes blank |
| `acquired_disposed` | XML `<transactionAcquiredDisposedCode>` | A=acquired, D=disposed |

The AI will likely note that `price_per_share` can be blank for non-market transactions (grants, gifts), and that the price field has different names in different schema versions — we'll explore that in Step 2.

Write this schema down. It's your target for Step 3.
:::

---

:::{important}
- [ ] You can explain in two sentences what a Form 4 filing is and why it's filed
- [ ] You understand the difference between non-derivative (stock) and derivative (option) transactions
- [ ] You have a proposed column schema for your output table
- [ ] You noticed that the price field might be named differently in different files
:::

---

**Next: [Step 2 – Discover the Quirks](step2-discover-quirks.md) →**
