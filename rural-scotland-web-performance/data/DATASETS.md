# Dataset Information

## Primary Dataset — HTTP Archive

**Source:** [HTTP Archive on Kaggle](https://www.kaggle.com/datasets/httparchive/web-page-performance)

**What it contains:**
Real performance measurements from 81,000+ page loads, including:
- `page_load_time_ms` — full page load time
- `ttfb_ms` — Time To First Byte
- `connection_speed_mbps` — simulated connection speed
- `cdn_provider` — which CDN/edge provider the site uses
- `total_transfer_kb` — page size

**Why this dataset:**
- Large enough for statistically meaningful results at < 20 Mbps
- Publicly licensed for research
- Includes all fields needed for analysis
- Well documented

**Download Instructions:**
1. Go to [Kaggle link](https://www.kaggle.com/datasets/httparchive/web-page-performance)
2. Create free account (if needed)
3. Click Download
4. Save as `http_archive_raw.csv`
5. Place in `data/` folder

---

## Connection Speed Reference

**Source:** Ofcom Connected Nations Report 2023

- **Western Isles (rural):** 15–20 Mbps
- **UK national average:** 52 Mbps
- **Major cities (Glasgow):** 67 Mbps

**Why 20 Mbps threshold:** Matches upper end of rural Scottish broadband speeds

---

## Generated Files

After running all Python scripts, these files will be created in `data/`:

| File | Description | Rows |
|------|-------------|------|
| `http_archive_cleaned.csv` | Full cleaned dataset | 840,000 |
| `rural_filtered.csv` | Connections < 20 Mbps | 94,000 |
| `rural_edge_group.csv` | Edge computing records | 18,000 |
| `rural_cdn_group.csv` | CDN records | 63,000 |
| `band_very_slow.csv` | < 10 Mbps | 22,000 |
| `band_slow.csv` | 10–15 Mbps | 31,000 |
| `band_moderate_slow.csv` | 15–20 Mbps | 41,000 |

All CSV files and `charts/` folder are excluded from Git (see `.gitignore`).
Regenerate locally by running the Python scripts.
