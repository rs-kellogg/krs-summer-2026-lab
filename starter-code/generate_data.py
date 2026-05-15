"""
generate_data.py — generates the synthetic firms.csv used in the lab.

Run this script if you want to regenerate the data:
    python starter-code/generate_data.py
"""

import csv
import random
import os

random.seed(42)

firms = [f'F{i:03d}' for i in range(1, 51)]
years = list(range(2018, 2023))

rows = []
for firm_id in firms:
    base_revenue = random.randint(500_000, 8_000_000)
    base_assets = base_revenue * random.uniform(0.8, 3.0)
    for year in years:
        revenue = round(base_revenue * random.uniform(0.85, 1.20), 2)
        cost = round(revenue * random.uniform(0.60, 0.82), 2)
        assets = round(base_assets * random.uniform(0.90, 1.15), 2)
        rows.append({
            'firm_id': firm_id,
            'year': year,
            'revenue': revenue,
            'cost': cost,
            'assets': assets,
        })

output_path = os.path.join(os.path.dirname(__file__), 'data', 'firms.csv')
with open(output_path, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['firm_id', 'year', 'revenue', 'cost', 'assets'])
    writer.writeheader()
    writer.writerows(rows)

print(f'Generated {len(rows)} rows → {output_path}')
