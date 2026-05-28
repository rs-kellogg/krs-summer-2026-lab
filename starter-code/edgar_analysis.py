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
