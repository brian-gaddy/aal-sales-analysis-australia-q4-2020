from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression

INPUT_PATH = Path("data/processed/aal_sales_q4_2020_clean.csv")
OUTPUT_PATH = Path("data/processed/state_sales_forecast.csv")


def forecast_state_sales(df, horizon_days=30):
    daily = df.groupby(["State", "Date"], as_index=False)["Sales"].sum()
    daily["Date"] = pd.to_datetime(daily["Date"])
    forecasts = []
    for state, group in daily.groupby("State"):
        group = group.sort_values("Date")
        x = (group["Date"] - group["Date"].min()).dt.days.to_numpy().reshape(-1, 1)
        model = LinearRegression().fit(x, group["Sales"])
        start = int(x.max()) + 1
        future_x = pd.Series(range(start, start + horizon_days)).to_numpy().reshape(-1, 1)
        future_dates = pd.date_range(group["Date"].max() + pd.Timedelta(days=1), periods=horizon_days)
        predicted = model.predict(future_x).clip(min=0)
        forecasts.extend({"State": state, "Date": date, "Forecast_Sales": value} for date, value in zip(future_dates, predicted))
    return pd.DataFrame(forecasts)


def main():
    df = pd.read_csv(INPUT_PATH, parse_dates=["Date"])
    forecast = forecast_state_sales(df)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    forecast.to_csv(OUTPUT_PATH, index=False)
    print(f"Saved {len(forecast):,} forecast rows to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
