# Setting Up Python for Analysis Scripts

## Step 1: Install Anaconda

Download from [anaconda.com](https://www.anaconda.com/download) — choose Windows version.
Anaconda installs Python and all required libraries (pandas, numpy, matplotlib, seaborn, jupyter).

## Step 2: Download the Dataset

See [data/DATASETS.md](../data/DATASETS.md) for download instructions.

**File must be:**
- Named: `http_archive_raw.csv`
- Location: `data/` folder

## Step 3: Run the Scripts

### Option A: VS Code (Recommended)
1. Open VS Code
2. File → Open Folder → select `rural-scotland-web-performance`
3. Click `.py` file in `notebooks/` folder
4. Press Run button (triangle icon) at top right
5. Select Anaconda Python when prompted

### Option B: Command Line
```bash
python notebooks/01_data_cleaning.py
python notebooks/02_filtering.py
python notebooks/03_analysis_charts.py
```

### Option C: Jupyter Notebook
1. Open Anaconda Navigator
2. Launch Jupyter Notebook
3. Navigate to `notebooks/` folder
4. Open and run `.py` files

## Output

- **CSV files:** `data/` folder (filtered datasets)
- **Charts:** `data/charts/` folder (PNG images)

1. Open Anaconda Navigator from your Start menu
2. Click Launch next to Jupyter Notebook
3. A browser window opens showing your files
4. Navigate to the notebooks/ folder
5. Click on any script to open it
6. Press Shift + Enter to run each block of code

---

## Step 4 — Run the scripts in this order

Each script saves output files that the next one needs.
Run them in order or the later ones will not work.

```
1. python 01_data_cleaning.py
   Reads the raw CSV and removes bad rows.
   Saves: data/http_archive_cleaned.csv

2. python 02_filtering.py
   Keeps only slow connections below 20 Mbps.
   Saves: data/rural_filtered.csv and several group files

3. python 03_analysis_charts.py
   Calculates the statistics and draws the three charts.
   Saves: data/charts/ folder with PNG images
```

---

## If you see an error saying a library is missing

Open a terminal in VS Code (press Ctrl and the backtick key) and type:

```bash
pip install pandas numpy matplotlib seaborn
```

Press Enter and wait for it to finish, then try running the script again.

---

## What the output looks like

After all three scripts finish, your data/ folder will contain:

| File                              | What it is                          |
|-----------------------------------|-------------------------------------|
| http_archive_cleaned.csv          | Cleaned full dataset                |
| rural_filtered.csv                | Slow connections only (<20 Mbps)    |
| rural_edge_group.csv              | Edge computing records              |
| rural_cdn_group.csv               | CDN records                         |
| band_very_slow.csv                | Connections below 10 Mbps           |
| band_slow.csv                     | Connections 10 to 15 Mbps           |
| band_moderate_slow.csv            | Connections 15 to 20 Mbps           |
| charts/chart1_load_time.png       | Chart for report section 6.1        |
| charts/chart2_ttfb.png            | Chart for report section 6.2        |
| charts/chart3_speed_bands.png     | Chart for report section 6.3        |
