# Contributing to Rural Scotland Web Performance Project

## Project Overview

This is a research project analyzing web performance in rural Scotland. It consists of:
- **Data analysis** (Python notebooks)
- **Demonstration website** (React + Cloudflare)
- **Comparison** of edge computing vs CDN technologies

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/[your-username]/rural-scotland-web-performance.git
   cd rural-scotland-web-performance
   ```

2. **Set up your environment**
   - For Python: See [notebooks/SETUP.md](notebooks/SETUP.md)
   - For web development: Install Node.js from [nodejs.org](https://nodejs.org)

3. **Download the dataset**
   - See [data/DATASETS.md](data/DATASETS.md) for instructions
   - Save as `http_archive_raw.csv` in `data/` folder

## Project Structure

- **notebooks/** — Python analysis scripts (run in order: 01 → 02 → 03)
- **demo-site/** — React demonstration website
- **workers/** — Cloudflare Workers edge computing script
- **data/** — Datasets and generated outputs (CSV files excluded from Git)

## Making Changes

### For Data Analysis

1. Create a branch: `git checkout -b feature/analysis-improvement`
2. Edit Python files in `notebooks/`
3. Test by running scripts: `python notebooks/01_data_cleaning.py`
4. Update documentation if methodology changes
5. Commit with clear messages: `git commit -m "Improve data cleaning logic"`

### For Demo Website

1. Create a branch: `git checkout -b feature/website-improvement`
2. Edit files in `demo-site/src/`
3. Test locally: `npm start` inside `demo-site/`
4. Build before committing: `npm run build`
5. Commit changes

### For Deployment Scripts

1. Create a branch: `git checkout -b feature/deployment-improvement`
2. Edit `workers/worker.js` or deployment configs
3. Test deployment following [workers/DEPLOY_WORKERS.md](workers/DEPLOY_WORKERS.md)
4. Commit changes

## Commit Messages

Keep commit messages clear and concise:

```
Fix data cleaning null values
Improve TTFB performance metrics
Update README with new findings
Add error handling to worker.js
```

## Code Style

- **Python:** PEP 8 (clear variable names, docstrings for functions)
- **JavaScript/React:** Use standard formatting, comment WHY not WHAT
- **Documentation:** Keep concise, use clear headings, include examples

## Testing

### Python Scripts

```bash
python notebooks/01_data_cleaning.py
python notebooks/02_filtering.py
python notebooks/03_analysis_charts.py
```

Verify output files are created in `data/` and charts appear in `data/charts/`.

### React Website

```bash
cd demo-site
npm install
npm start
```

Test in browser at `http://localhost:3000`

## Documentation

- Keep README.md updated with major changes
- Document new datasets in [data/DATASETS.md](data/DATASETS.md)
- Update deployment guides if procedures change
- Add comments for complex logic

## Reporting Issues

If you find bugs or have suggestions:
1. Check existing issues first
2. Create a new issue with:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, Node version, etc.)

## Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request with:
   - Clear title and description
   - Reference to related issues
   - List of changes made

## Questions?

For academic or research questions, contact the supervisor: **Nuzhat Younis** at University of the West of Scotland.

---

**Thank you for contributing to this research project!**
