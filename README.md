# AAL Sales Analysis — Australia Q4 2020

## Overview

This project analyzes Q4 2020 sales performance for AAL, an Australian apparel retailer. It identifies high- and low-performing states, compares customer segments, evaluates time-of-day demand, and translates findings into sales and marketing recommendations.

## Key Findings

- **VIC** is the top-performing state with **$105.565M** in sales.
- **WA** is the lowest-performing state with **$22.153M** in sales.
- **Men** are the highest-revenue customer group at **$85.750M**.
- **Seniors** are the lowest-revenue customer group at **$84.038M**.
- **Morning** is the strongest sales period at **$114.208M**.
- Q4 sales totaled **$340.303M** across **7,560 records** and **136,121 units**.

## Business Recommendations

1. Protect and scale VIC by using its sales patterns as a benchmark for inventory and promotional execution.
2. Launch localized growth programs in WA and other lower-revenue states using segment-specific offers and store-level targets.
3. Use customer-group targeting for retention, upsell, and Next Best Offer campaigns.
4. Schedule high-value campaigns around morning demand while testing offers designed to lift evening sales.
5. Track daily, weekly, and monthly performance to measure campaign impact and adjust sales programs quickly.

## Project Upgrades

This portfolio version extends the original course project with:

- A reproducible Python analysis pipeline in `src/analyze_sales.py`
- An interactive Streamlit dashboard in `app.py`
- State-level linear trend forecasting in `src/forecast_sales.py`
- Automated data-quality tests with pytest
- GitHub Actions continuous integration
- Processed analytical summary tables
- Executive project documentation

## Repository Structure

```text
.
├── app.py
├── src/
│   ├── analyze_sales.py
│   └── forecast_sales.py
├── tests/
│   └── test_analysis.py
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── figures/
├── docs/
├── .github/workflows/ci.yml
├── PROJECT_REPORT.md
├── PROBLEM_STATEMENT.md
└── requirements.txt
```

## Run the Analysis

```bash
pip install -r requirements.txt
python src/analyze_sales.py
python src/forecast_sales.py
```

## Launch the Dashboard

```bash
streamlit run app.py
```

## Run Tests

```bash
pytest -q
```

## Technologies

Python · pandas · NumPy · Matplotlib · Seaborn · Plotly · Streamlit · scikit-learn · Jupyter · GitHub Actions

## Portfolio Relevance

This project demonstrates retail analytics, data wrangling, descriptive statistics, time-series reporting, executive dashboard development, basic forecasting, automated testing, and business recommendation development.
