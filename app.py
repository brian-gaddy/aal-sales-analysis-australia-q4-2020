import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="AAL Sales Dashboard", layout="wide")
st.title("AAL Sales Analysis — Australia Q4 2020")

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/aal_sales_q4_2020_clean.csv", parse_dates=["Date"])

df = load_data()
states = sorted(df["State"].unique())
selected_states = st.sidebar.multiselect("State", states, default=states)
selected_groups = st.sidebar.multiselect("Customer group", sorted(df["Age_Group"].unique()), default=sorted(df["Age_Group"].unique()))
filtered = df[df["State"].isin(selected_states) & df["Age_Group"].isin(selected_groups)]

c1, c2, c3 = st.columns(3)
c1.metric("Total Sales", f"${filtered['Sales'].sum()/1_000_000:,.1f}M")
c2.metric("Units", f"{filtered['Unit'].sum():,}")
c3.metric("Records", f"{len(filtered):,}")

state_sales = filtered.groupby("State", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False)
group_sales = filtered.groupby("Age_Group", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False)
daily_sales = filtered.groupby("Date", as_index=False)["Sales"].sum()
time_sales = filtered.groupby("Time", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False)

st.plotly_chart(px.bar(state_sales, x="State", y="Sales", title="Sales by State"), use_container_width=True)
st.plotly_chart(px.bar(group_sales, x="Age_Group", y="Sales", title="Sales by Customer Group"), use_container_width=True)
st.plotly_chart(px.line(daily_sales, x="Date", y="Sales", title="Daily Sales Trend", markers=True), use_container_width=True)
st.plotly_chart(px.bar(time_sales, x="Time", y="Sales", title="Sales by Time of Day"), use_container_width=True)

st.subheader("Executive Interpretation")
st.write("Use the state and customer-group filters to compare market performance. VIC is the Q4 revenue leader, while WA is the lowest-revenue state. Morning is the strongest sales period, supporting targeted campaign timing and localized growth programs.")
