# Data

This lab uses real SEC EDGAR Form 4 filings hosted on the Kellogg Linux Cluster.

**Location on KLC:** `/kellogg/data/EDGAR/4/2003/`

**About Form 4:** A Form 4 is filed with the SEC whenever a corporate insider
(director, officer, or 10%+ shareholder) buys or sells company stock. Each file
is a plain-text document containing filing metadata and an embedded
`<ownershipDocument>` XML block with transaction details.

**File naming:** `{issuer_cik}_{form_type}_{accession_number}.txt`

**Transaction codes used in this lab:**

| Code | Meaning |
|------|---------|
| `P` | Open-market purchase |
| `S` | Open-market sale |
| `A` | Grant or award (not a market transaction) |
| `J` | Other |

The 2003 directory contains approximately 324,000 files. The starter script
processes the first 500 (sorted alphabetically) as a representative sample.
