"""Step 3: Calculate statistics and generate comparison charts.

Reads filtered edge and CDN datasets, computes key metrics, and produces
three charts comparing performance across connection speeds.

Run after 02_filtering.py completes.
Output: Three PNG charts saved to data/charts/
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import os

# Chart configuration
sns.set_theme(style='whitegrid', palette='muted')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['figure.dpi'] = 100

COLOUR_EDGE = '#1D9E75'
COLOUR_CDN = '#378ADD'

os.makedirs('../data/charts', exist_ok=True)

# Load filtered datasets
print('Loading filtered datasets...')
edge = pd.read_csv('../data/rural_edge_group.csv')
cdn = pd.read_csv('../data/rural_cdn_group.csv')
very_slow = pd.read_csv('../data/band_very_slow.csv')
slow_band = pd.read_csv('../data/band_slow.csv')
mod_slow = pd.read_csv('../data/band_moderate_slow.csv')
print(f'Edge: {len(edge):,} records | CDN: {len(cdn):,} records')
print()

# Calculate and display key statistics
def print_stats(df, label):
    """Print mean, median, std for load time and TTFB."""
    load_mean = df['page_load_time_ms'].mean() / 1000
    load_median = df['page_load_time_ms'].median() / 1000
    load_std = df['page_load_time_ms'].std() / 1000
    ttfb_mean = df['ttfb_ms'].mean()
    ttfb_median = df['ttfb_ms'].median()
    print(f'{label}:')
    print(f'  Load: {load_mean:.2f}s mean, {load_median:.2f}s median, {load_std:.2f}s std')
    print(f'  TTFB: {ttfb_mean:.0f}ms mean, {ttfb_median:.0f}ms median')
    print()

print_stats(edge, 'Edge computing')
print_stats(cdn, 'CDN')

load_improvement = (cdn['page_load_time_ms'].mean() - edge['page_load_time_ms'].mean()) / cdn['page_load_time_ms'].mean() * 100
ttfb_improvement = (cdn['ttfb_ms'].mean() - edge['ttfb_ms'].mean()) / cdn['ttfb_ms'].mean() * 100
print(f'Edge improvement vs CDN: {load_improvement:.1f}% load time, {ttfb_improvement:.1f}% TTFB')
print()

# Chart 1: Load time comparison
print('Creating Chart 1: Load time comparison...')
labels = ['Mean load time', 'Median load time']
edge_values = [edge['page_load_time_ms'].mean() / 1000, edge['page_load_time_ms'].median() / 1000]
cdn_values = [cdn['page_load_time_ms'].mean() / 1000, cdn['page_load_time_ms'].median() / 1000]

fig, ax = plt.subplots(figsize=(8, 5))
x, width = np.arange(len(labels)), 0.35

bars_edge = ax.bar(x - width / 2, edge_values, width, label='Edge computing', color=COLOUR_EDGE, zorder=3, edgecolor='white', linewidth=0.5)
bars_cdn = ax.bar(x + width / 2, cdn_values, width, label='CDN', color=COLOUR_CDN, zorder=3, edgecolor='white', linewidth=0.5)

for bar in list(bars_edge) + list(bars_cdn):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.06, f'{bar.get_height():.2f}s', ha='center', va='bottom', fontsize=10)

ax.set_ylabel('Seconds')
ax.set_title('Page load time — Edge computing vs CDN\n(connections below 20 Mbps)')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc='upper right')
ax.set_ylim(0, max(cdn_values) * 1.3)
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.1fs'))

plt.tight_layout()
plt.savefig('../data/charts/chart1_load_time_comparison.png', dpi=150)
plt.close()
print('✓ Chart 1 saved')
print()

# Chart 2: Time to First Byte
print('Creating Chart 2: TTFB comparison...')
ttfb_edge = edge['ttfb_ms'].mean()
ttfb_cdn = cdn['ttfb_ms'].mean()
improvement = (ttfb_cdn - ttfb_edge) / ttfb_cdn * 100

fig, ax = plt.subplots(figsize=(6, 5))
bars = ax.bar(['Edge computing', 'CDN'], [ttfb_edge, ttfb_cdn], color=[COLOUR_EDGE, COLOUR_CDN], width=0.45, zorder=3, edgecolor='white', linewidth=0.5)

for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 6, f'{bar.get_height():.0f}ms', ha='center', va='bottom', fontsize=12, fontweight='bold')

ax.text(0.5, 0.93, f'Edge {improvement:.0f}% faster', transform=ax.transAxes, ha='center', fontsize=10, color='#444444')
ax.set_ylabel('Milliseconds (ms)')
ax.set_title('Time to First Byte (TTFB)\nEdge computing vs CDN (connections below 20 Mbps)')
ax.set_ylim(0, max(ttfb_cdn, ttfb_edge) * 1.35)

plt.tight_layout()
plt.savefig('../data/charts/chart2_ttfb_comparison.png', dpi=150)
plt.close()
print('✓ Chart 2 saved')
print()

# Chart 3: Speed band comparison
print('Creating Chart 3: Speed band comparison...')

def get_band_mean(df, low, high=None):
    """Return mean load time in seconds for a speed band."""
    if high is None:
        subset = df[df['connection_speed_mbps'] < low]
    else:
        subset = df[(df['connection_speed_mbps'] >= low) & (df['connection_speed_mbps'] < high)]
    return subset['page_load_time_ms'].mean() / 1000

band_labels = ['Below 10 Mbps', '10 to 15 Mbps', '15 to 20 Mbps']
edge_by_band = [get_band_mean(edge, 10), get_band_mean(edge, 10, 15), get_band_mean(edge, 15, 20)]
cdn_by_band = [get_band_mean(cdn, 10), get_band_mean(cdn, 10, 15), get_band_mean(cdn, 15, 20)]

fig, ax = plt.subplots(figsize=(9, 5.5))
x, width = np.arange(len(band_labels)), 0.35

b1 = ax.bar(x - width / 2, edge_by_band, width, label='Edge computing', color=COLOUR_EDGE, zorder=3, edgecolor='white', linewidth=0.5)
b2 = ax.bar(x + width / 2, cdn_by_band, width, label='CDN', color=COLOUR_CDN, zorder=3, edgecolor='white', linewidth=0.5)

for bar in list(b1) + list(b2):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.08, f'{bar.get_height():.2f}s', ha='center', va='bottom', fontsize=9)

ax.set_ylabel('Seconds')
ax.set_title('Mean load time by connection speed band\nEdge computing vs CDN (connections below 20 Mbps)')
ax.set_xticks(x)
ax.set_xticklabels(band_labels)
ax.legend(loc='upper right')
ax.set_ylim(0, max(cdn_by_band) * 1.3)
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.1fs'))

plt.tight_layout()
plt.savefig('../data/charts/chart3_speed_band_comparison.png', dpi=150)
plt.show()
print('Chart 3 saved to data/charts/chart3_speed_band_comparison.png')
print()

# ── 6. Final summary ──────────────────────────────────────────

print('=' * 55)
print('All analysis complete.')
print('Three charts saved to data/charts/')
print()
print('Key numbers for your report:')
print(f'  Edge mean load time : {edge["page_load_time_ms"].mean()/1000:.2f}s')
print(f'  CDN  mean load time : {cdn["page_load_time_ms"].mean()/1000:.2f}s')
print(f'  Improvement         : {load_improvement:.1f}%')
print(f'  Edge TTFB mean      : {edge["ttfb_ms"].mean():.0f}ms')
print(f'  CDN  TTFB mean      : {cdn["ttfb_ms"].mean():.0f}ms')
print(f'  TTFB improvement    : {ttfb_improvement:.1f}%')
print('=' * 55)
