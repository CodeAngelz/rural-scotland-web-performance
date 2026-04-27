# Web Performance Analysis for Rural Scotland
Comparing Edge Computing and CDN Solutions Using Open-Source Network Data

**Author:** Michael Emeka Ibeh | **Banner ID:** B01767356 | **Institution:** University of the West of Scotland | **Programme:** MSc Information Technology with Web Development | **Supervisor:** Nuzhat Younis

---

## Research Question

Rural Scotland has significantly slower internet than urban areas — the Western Isles averages 15–20 Mbps while Glasgow averages 67 Mbps. When internet connection itself is slow, does edge computing actually perform better than a standard CDN?

## Key Findings

| Metric              | Edge computing | CDN    | Difference          |
|---------------------|----------------|--------|---------------------|
| Mean load time      | 4.82s          | 5.31s  | Edge 9.2% faster    |
| Median load time    | 3.94s          | 4.38s  | Edge 10.0% faster   |
| Time to First Byte  | 312ms          | 489ms  | Edge 36% faster     |
| Std deviation       | 2.17s          | 2.43s  | Edge more consistent|

**Conclusion:** Edge computing provides modest but consistent improvements on slow connections, with the largest benefits for websites with server-side logic and connections in the 15–20 Mbps range. For connections below 10 Mbps, reducing page weight matters more than switching infrastructure.

---

## Structure

```
rural-scotland-web-performance/
├── README.md                    This file
├── .gitignore                   Git configuration
│
├── data/
│   └── DATASETS.md              Where to download datasets
│
├── notebooks/                   Python analysis scripts
│   ├── SETUP.md                 Installation instructions
│   ├── 01_data_cleaning.py      Clean raw dataset
│   ├── 02_filtering.py          Filter for rural conditions
│   └── 03_analysis_charts.py    Generate analysis and charts
│
├── demo-site/                   React demonstration website
│   ├── DEPLOY_CDN.md            Deploy via Cloudflare Pages (CDN)
│   ├── package.json
│   ├── public/index.html
│   └── src/
│       ├── App.jsx              Main page component
│       ├── index.jsx            React entry point
│       └── styles.css           Styling
│
└── workers/                     Cloudflare Workers edge script
    ├── DEPLOY_WORKERS.md        Deploy via Cloudflare Workers
    ├── worker.js                Edge computing handler
    └── wrangler.toml            Deployment configuration
```

---

## Quick Start

### Run Python Analysis

1. **Install dependencies:** Download Anaconda from [anaconda.com](https://www.anaconda.com/download) (includes Python, Pandas, Matplotlib, NumPy)
2. **Download dataset:** See [data/DATASETS.md](data/DATASETS.md)
3. **Run scripts:**
   ```bash
   python notebooks/01_data_cleaning.py
   python notebooks/02_filtering.py
   python notebooks/03_analysis_charts.py
   ```
4. **Output:** Charts are saved to `data/charts/`

### Deploy Demo Website (CDN)

1. `cd demo-site && npm install && npm run build`
2. Go to [dash.cloudflare.com](https://dash.cloudflare.com)
3. Drag the `build/` folder to Cloudflare Pages
4. Your site is live at `https://[project-name].pages.dev`

### Deploy Demo Website (Edge Computing)

1. Install Node.js and Wrangler: `npm install -g wrangler`
2. `wrangler login`
3. `cd demo-site && npm run build && cd ../workers`
4. Update `wrangler.toml` with your KV namespace ID
5. `wrangler deploy`

---

## Methodology

- **Dataset:** 81,000 real performance records from HTTP Archive (connections < 20 Mbps)
- **Rural threshold:** < 20 Mbps based on Ofcom Connected Nations Report 2023
- **Providers tested:** Cloudflare Workers (edge), AWS Lambda@Edge, Fastly Compute vs Cloudflare CDN, AWS CloudFront, Akamai
- **Metrics:** Load time, Time to First Byte (TTFB), consistency

---

## License

This project is provided for educational and research purposes.

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

- **CDN version (Cloudflare Pages):** https://skyeandglen.pages.dev
- **Edge computing version (Cloudflare Workers):** https://skyeandglen.workers.dev

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
