"""Step 1: Clean the raw HTTP Archive dataset.

Downloads the raw HTTP Archive CSV file and removes invalid/missing data.
Output is saved to data/http_archive_cleaned.csv

Run this first before 02_filtering.py and 03_analysis_charts.py
"""

import pandas as pd
import numpy as np

DATA_PATH = '../data/http_archive_raw.csv'

print('Loading dataset...')
df = pd.read_csv(DATA_PATH, low_memory=False)
print(f'  Rows: {len(df):,} | Columns: {len(df.columns)}')
print()

# Keep only the columns needed for analysis
COLUMNS_NEEDED = [
    'page_load_time_ms',      # Full page load time in milliseconds
    'ttfb_ms',                # Time To First Byte in milliseconds
    'connection_speed_mbps',  # User's internet speed in Mbps
    'cdn_provider',           # Which CDN or edge provider the site uses
    'total_transfer_kb',      # Total size of the page in kilobytes
]
df = df[COLUMNS_NEEDED].copy()
print(f'Selected {len(df.columns)} columns')
print()

# Remove rows with missing speed data
rows_before = len(df)
df = df.dropna(subset=['connection_speed_mbps'])
print(f'Removed {rows_before - len(df):,} rows with missing speed data')

# Remove invalid values
df = df[df['page_load_time_ms'] > 0]
df = df[df['ttfb_ms'] > 0]
df = df[(df['connection_speed_mbps'] > 0) & (df['connection_speed_mbps'] <= 1000)]
print(f'Removed rows with impossible values | Remaining: {len(df):,}')
print()

# Normalize provider names
provider_map = {
    'cloudflare-workers': 'Cloudflare Workers',
    'cf-workers': 'Cloudflare Workers',
    'cloudflare': 'Cloudflare CDN',
    'cloudflare-cdn': 'Cloudflare CDN',
    'akamai technologies': 'Akamai',
    'amazon cloudfront': 'AWS CloudFront',
    'cloudfront': 'AWS CloudFront',
    'fastly-compute': 'Fastly Compute',
    'fastly': 'Fastly CDN',
    'aws-lambda-edge': 'AWS Lambda@Edge',
}
df['cdn_provider'] = df['cdn_provider'].str.strip().str.lower().replace(provider_map)
print('Provider names normalized')
print()

# Save cleaned data
OUTPUT_PATH = '../data/http_archive_cleaned.csv'
df.to_csv(OUTPUT_PATH, index=False)
print(f'Saved {len(df):,} rows to {OUTPUT_PATH}')
print('✓ Step 1 complete. Run 02_filtering.py next.')
