"""Step 2: Filter data for rural conditions and split by provider type.

Takes the cleaned dataset and keeps only records with connections below 20 Mbps
(matching rural Scottish broadband speeds). Splits results into:
  - Edge computing vs CDN groups
  - Three speed bands for detailed analysis

Run after 01_data_cleaning.py completes.
"""

import pandas as pd
import numpy as np

print('Loading cleaned dataset...')
df = pd.read_csv('../data/http_archive_cleaned.csv', low_memory=False)
print(f'  {len(df):,} rows loaded')
print()

# Filter for rural conditions (below 20 Mbps, per Ofcom Connected Nations 2023)
MAX_SPEED_MBPS = 20
rural = df[df['connection_speed_mbps'] < MAX_SPEED_MBPS].copy()
print(f'Filtered for < {MAX_SPEED_MBPS} Mbps: {len(rural):,} records ({len(rural) / len(df) * 100:.1f}% of full dataset)')
print()

# Create speed bands for breakdown analysis
very_slow = rural[rural['connection_speed_mbps'] < 10].copy()
slow = rural[(rural['connection_speed_mbps'] >= 10) & (rural['connection_speed_mbps'] < 15)].copy()
mod_slow = rural[(rural['connection_speed_mbps'] >= 15) & (rural['connection_speed_mbps'] < 20)].copy()

print('Speed bands:')
print(f'  < 10 Mbps : {len(very_slow):,} records')
print(f'  10-15 Mbps: {len(slow):,} records')
print(f'  15-20 Mbps: {len(mod_slow):,} records')
print()

# Split into technology groups
EDGE_PROVIDERS = ['Cloudflare Workers', 'Fastly Compute', 'AWS Lambda@Edge']
CDN_PROVIDERS = ['Cloudflare CDN', 'Akamai', 'Fastly CDN', 'AWS CloudFront']

edge = rural[rural['cdn_provider'].isin(EDGE_PROVIDERS)].copy()
cdn = rural[rural['cdn_provider'].isin(CDN_PROVIDERS)].copy()

print('Technology groups:')
print(f'  Edge computing: {len(edge):,} records')
print(f'  CDN           : {len(cdn):,} records')
print()

print('Edge computing breakdown:')
print(edge['cdn_provider'].value_counts())
print()
print('CDN breakdown:')
print(cdn['cdn_provider'].value_counts())
print()

# Quick comparison check
print('Mean load times:')
print(f'  Edge: {edge["page_load_time_ms"].mean() / 1000:.2f}s')
print(f'  CDN : {cdn["page_load_time_ms"].mean() / 1000:.2f}s')
print()
print('Mean TTFB:')
print(f'  Edge: {edge["ttfb_ms"].mean():.0f}ms')
print(f'  CDN : {cdn["ttfb_ms"].mean():.0f}ms')
print()

# Save filtered datasets
rural.to_csv('../data/rural_filtered.csv', index=False)
edge.to_csv('../data/rural_edge_group.csv', index=False)
cdn.to_csv('../data/rural_cdn_group.csv', index=False)
very_slow.to_csv('../data/band_very_slow.csv', index=False)
slow.to_csv('../data/band_slow.csv', index=False)
mod_slow.to_csv('../data/band_moderate_slow.csv', index=False)

print('Saved 6 filtered CSV files to data/')
print('✓ Step 2 complete. Run 03_analysis_charts.py next.')

print('All filtered files saved to the data/ folder:')
print('  rural_filtered.csv')
print('  rural_edge_group.csv')
print('  rural_cdn_group.csv')
print('  band_very_slow.csv')
print('  band_slow.csv')
print('  band_moderate_slow.csv')
print()
print('Step 2 complete. Now run 03_analysis_charts.py')
