import pandas as pd
import pytest
from src.analyze_sales import build_summaries, load_and_clean


def test_build_summaries_identifies_top_state():
    df = pd.DataFrame({
        "State": ["VIC", "VIC", "WA"],
        "Age_Group": ["Men", "Women", "Men"],
        "Time": ["Morning", "Evening", "Morning"],
        "Week": ["W1", "W1", "W1"],
        "Month": ["2020-10"] * 3,
        "Sales": [100, 200, 50],
    })
    summaries = build_summaries(df)
    assert summaries["state_sales_summary"].iloc[0]["State"] == "VIC"
    assert summaries["state_sales_summary"].iloc[0]["Sales"] == 300


def test_load_and_clean_rejects_missing_core_values(tmp_path):
    df = pd.DataFrame({
        "Date": ["2020-10-01"], "Time": ["Morning"], "State": ["VIC"],
        "Age_Group": ["Men"], "Unit": [1], "Sales": [None]
    })
    path = tmp_path / "bad.xlsx"
    df.to_excel(path, index=False)
    with pytest.raises(ValueError, match="missing values"):
        load_and_clean(path)
