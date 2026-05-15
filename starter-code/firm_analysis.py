"""
firm_analysis.py — starter script for the AI-Assisted Data Analysis Lab

This script loads firm-level financial data, computes derived metrics,
filters to larger firms, and writes an annual summary CSV.

Note: This is intentionally written in a flat, non-modular style with
hardcoded paths — improving it is the goal of the lab exercises.
"""

import pandas as pd

df = pd.read_csv('starter-code/data/firms.csv')

df['profit'] = df['revenue'] - df['cost']
df['profit_margin'] = df['profit'] / df['revenue']
df['roa'] = df['profit'] / df['assets']
df['asset_turnover'] = df['revenue'] / df['assets']

df = df[df['revenue'] > 1000000]

summary = df.groupby('year').agg(
    n_firms=('firm_id', 'count'),
    mean_profit_margin=('profit_margin', 'mean'),
    median_profit_margin=('profit_margin', 'median'),
    mean_roa=('roa', 'mean'),
    mean_asset_turnover=('asset_turnover', 'mean')
).reset_index()

summary = summary.round(4)

summary.to_csv('starter-code/output/summary.csv', index=False)
print('done')
