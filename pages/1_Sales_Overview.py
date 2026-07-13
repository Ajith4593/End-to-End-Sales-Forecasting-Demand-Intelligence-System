
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("superstore_processed.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Year"] = df["Order Date"].dt.year

st.title("Sales Overview Dashboard")

year_sales = (
    df.groupby("Year")["Sales"]
    .sum()
    .reset_index()
)

fig = px.bar(
    year_sales,
    x="Year",
    y="Sales",
    title="Total Sales By Year"
)

st.plotly_chart(fig, use_container_width=True)

monthly_sales = (
    df.groupby(
        pd.Grouper(
            key="Order Date",
            freq="M"
        )
    )["Sales"]
    .sum()
    .reset_index()
)

fig2 = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    title="Monthly Sales Trend"
)

st.plotly_chart(fig2, use_container_width=True)

region = st.selectbox(
    "Region",
    ["All"] + list(df["Region"].unique())
)

category = st.selectbox(
    "Category",
    ["All"] + list(df["Category"].unique())
)

filtered = df.copy()

if region != "All":
    filtered = filtered[
        filtered["Region"] == region
    ]

if category != "All":
    filtered = filtered[
        filtered["Category"] == category
    ]

st.dataframe(filtered.head(20))
