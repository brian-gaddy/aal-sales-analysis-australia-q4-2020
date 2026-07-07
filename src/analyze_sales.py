from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt

RAW_PATH = Path("data/raw/AusApparalSales4thQrt2020.xlsx")
PROCESSED_DIR = Path("data/processed")
FIGURES_DIR = Path("figures")
CORE_COLUMNS = ["Date", "Time", "State", "Age_Group", "Unit", "Sales"]


def load_and_clean(path=RAW_PATH):
    df = pd.read_excel(path)
    df = df.loc[:, ~df.columns.astype(str).str.startswith("Unnamed")].copy()
    df.columns = df.columns.str.strip()
    missing = [c for c in CORE_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    for col in ["Time", "State", "Age_Group"]:
        df[col] = df[col].astype(str).str.strip()
    df["Date"] = pd.to_datetime(df["Date"], errors="raise")
    if df[CORE_COLUMNS].isna().any().any():
        raise ValueError("Core analytical fields contain missing values.")
    if (df[["Unit", "Sales"]] < 0).any().any():
        raise ValueError("Unit and Sales must be non-negative.")
    df["Week"] = df["Date"].dt.to_period("W").astype(str)
    df["Month"] = df["Date"].dt.to_period("M").astype(str)
    df["Quarter"] = df["Date"].dt.to_period("Q").astype(str)
    return df


def build_summaries(df):
    return {
        "state_sales_summary": df.groupby("State", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False),
        "customer_group_sales_summary": df.groupby("Age_Group", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False),
        "time_of_day_sales_summary": df.groupby("Time", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False),
        "weekly_sales_summary": df.groupby("Week", as_index=False)["Sales"].sum(),
        "monthly_sales_summary": df.groupby("Month", as_index=False)["Sales"].sum(),
        "state_by_customer_group_sales": df.pivot_table(index="State", columns="Age_Group", values="Sales", aggfunc="sum").fillna(0),
    }


def save_outputs(df, summaries):
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DIR / "aal_sales_q4_2020_clean.csv", index=False)
    for name, table in summaries.items():
        table.to_csv(PROCESSED_DIR / f"{name}.csv", index=name == "state_by_customer_group_sales")

    state = summaries["state_sales_summary"]
    plt.figure(figsize=(9, 5))
    plt.bar(state["State"], state["Sales"])
    plt.title("Total Sales by State — AAL Q4 2020")
    plt.xlabel("State")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "sales_by_state.png", dpi=180)
    plt.close()

    metrics = {
        "rows": len(df),
        "total_sales": float(df["Sales"].sum()),
        "total_units": int(df["Unit"].sum()),
        "top_state": state.iloc[0].to_dict(),
        "bottom_state": state.iloc[-1].to_dict(),
    }
    (PROCESSED_DIR / "key_metrics.json").write_text(json.dumps(metrics, indent=2))


def main():
    df = load_and_clean()
    summaries = build_summaries(df)
    save_outputs(df, summaries)
    print("Analysis complete. Processed tables and figures were regenerated.")


if __name__ == "__main__":
    main()
