# Project Report: AAL Sales Analysis — Australia Q4 2020

## Executive Summary

This project analyzes 7,560 Q4 2020 sales records for AAL, an Australian apparel retailer. Total sales were $340.303M across 136,121 units. The analysis supports two business decisions: identify the highest-revenue states and develop sales programs for lower-revenue states.

## Findings

VIC led state performance with $105.565M in sales, while WA generated $22.153M. Men were the highest-revenue customer group at $85.750M; Seniors were the lowest at $84.038M. Morning was the strongest sales period at $114.208M, while evening was the weakest at $112.088M.

## Data Engineering and Quality

The reproducible analysis pipeline removes non-data helper columns, standardizes column names and categorical whitespace, validates required fields, converts dates, rejects missing core analytical values, rejects negative unit or sales values, and derives weekly, monthly, and quarterly reporting fields.

## Analytics Architecture

- `src/analyze_sales.py` regenerates cleaned data, analytical summaries, metrics, and figures.
- `app.py` provides an interactive Streamlit dashboard with state and customer-group filters.
- `src/forecast_sales.py` provides a transparent state-level linear trend baseline forecast.
- `tests/test_analysis.py` validates data-quality controls and summary logic.
- GitHub Actions runs pytest on pushes and pull requests.

## Recommendations

Use VIC as a benchmark for inventory and promotional execution. Build localized growth programs for WA and other lower-revenue states. Apply segment-specific retention and upsell campaigns. Concentrate high-value campaigns in morning periods while running controlled tests to improve evening demand. Review weekly and monthly scorecards to measure program lift.

## Forecasting Limitation

The forecasting module is intentionally a baseline model. Q4 contains only one quarter of history and may include seasonal effects, so forecasts should not be treated as production demand plans. A stronger version should use multiple years of sales history, holiday and promotion features, and backtesting with MAE or MAPE.

## Next Steps

Future work should add promotion and margin data, expand the historical window, compare forecasting algorithms, deploy the Streamlit dashboard, and add campaign lift or A/B testing analysis.
