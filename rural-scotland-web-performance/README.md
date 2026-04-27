# Web Performance Analysis for Rural Scotland
## Comparing Edge Computing and CDN Solutions Using Open-Source Network Data

**Student:** Michael Emeka Ibeh
**Banner ID:** B01767356
**Programme:** MSc Information Technology with Web Development
**University:** University of the West of Scotland
**Supervisor:** Nuzhat Younis
**Submission Year:** 2026

---

## About this project

People living in rural Scotland deal with internet speeds far below the national
average. The Western Isles averages 15 to 20 Mbps while cities like Glasgow
average around 67 Mbps.

This project asks one question: when the internet connection itself is slow,
does edge computing actually perform better than a standard CDN?

To answer it, I analysed 81,000 real performance records from the HTTP Archive
dataset, filtering for connections below 20 Mbps to match rural Scottish
conditions. I also built and deployed a simple demonstration website using both
Cloudflare Workers (edge computing) and Cloudflare Pages (CDN) to understand
each technology from a developer's point of view.

---

## Key findings

| Metric              | Edge computing | CDN    | Difference          |
|---------------------|----------------|--------|---------------------|
| Mean load time      | 4.82s          | 5.31s  | Edge 9.2% faster    |
| Median load time    | 3.94s          | 4.38s  | Edge 10.0% faster   |
| Time to First Byte  | 312ms          | 489ms  | Edge 36% faster     |
| Std deviation       | 2.17s          | 2.43s  | Edge more consistent|

**Main conclusion:** Edge computing provides a consistent but modest improvement
on slow connections. The benefit is largest for websites with server-side logic
and for connections in the 15 to 20 Mbps range. For connections below 10 Mbps,
reducing page weight matters more than switching infrastructure.

---

## Repository structure

```
rural-scotland-web-performance/
│
├── README.md                        This file
├── .gitignore                       Files Git should not upload
│
├── notebooks/                       Python analysis scripts
│   ├── SETUP.md                     How to install and run Python scripts
│   ├── 01_data_cleaning.py          Step 1 — clean the raw dataset
│   ├── 02_filtering.py              Step 2 — filter for rural conditions
│   └── 03_analysis_charts.py        Step 3 — statistics and charts
│
├── demo-site/                       React demonstration website
│   ├── DEPLOY_CDN.md                How to deploy via Cloudflare Pages
│   ├── package.json                 Project dependencies
│   ├── public/
│   │   └── index.html               HTML entry point
│   └── src/
│       ├── index.jsx                React entry point
│       ├── App.jsx                  Main page — edit content here
│       └── styles.css               All visual styling
│
├── workers/                         Cloudflare Workers edge script
│   ├── DEPLOY_WORKERS.md            How to deploy via Cloudflare Workers
│   ├── worker.js                    Edge computing handler
│   └── wrangler.toml                Deployment configuration
│
└── data/
    └── DATASETS.md                  Where to download the dataset
```

---

## How to run the Python analysis

### Requirements
- Anaconda — download from https://www.anaconda.com/download
  (This installs Python, Pandas, Matplotlib, NumPy and Jupyter all at once)

### Steps
1. Download the dataset — see data/DATASETS.md for the link
2. Save it as `http_archive_raw.csv` inside the `data/` folder
3. Open Anaconda Navigator and launch Jupyter Notebook
4. Navigate to the `notebooks/` folder and run scripts in order:

```bash
python notebooks/01_data_cleaning.py
python notebooks/02_filtering.py
python notebooks/03_analysis_charts.py
```

Charts are saved automatically to `data/charts/`

---

## How to run the demonstration website locally

### Requirements
- Node.js — download from https://nodejs.org

### Steps

```bash
cd demo-site
npm install
npm start
```

Then open http://localhost:3000 in your browser.

---

## Live deployments

- **CDN version (Cloudflare Pages):** https://skyeandglen-uws.pages.dev
- **Edge computing version (Cloudflare Workers):** https://skyeandglen.skyeandglen-uws.workers.dev

These are demonstration sites only. They collect no user data and take no
real bookings.

---

## Technologies used

| Area                 | Technology                        |
|----------------------|-----------------------------------|
| Data analysis        | Python 3, Pandas, NumPy           |
| Charts               | Matplotlib, Seaborn               |
| Notebook environment | Jupyter Notebook (via Anaconda)   |
| Front-end framework  | React 18                          |
| Styling              | Plain CSS                         |
| CDN deployment       | Cloudflare Pages                  |
| Edge deployment      | Cloudflare Workers                |
| Version control      | Git / GitHub                      |

---

## References

Ofcom (2023) Connected Nations Report 2023.
https://www.ofcom.org.uk/research-and-data/telecoms-research/connected-nations

HTTP Archive dataset via Kaggle:
https://www.kaggle.com/datasets/httparchive/web-page-performance

---

## Contact

Michael Emeka Ibeh
B01767356@studentmail.uws.ac.uk
University of the West of Scotland
