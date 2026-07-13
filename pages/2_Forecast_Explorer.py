import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Forecast Explorer")

# Load forecast data
forecast_df = pd.read_csv("forecast_table.csv")

st.subheader("Forecast Data")
st.dataframe(forecast_df)

# Select segment
segment = st.selectbox(
    "Select Segment",
    forecast_df["Segment"].unique()
)

# Filter selected segment
filtered_df = forecast_df[forecast_df["Segment"] == segment]

# Convert to long format
plot_df = filtered_df.melt(
    id_vars="Segment",
    var_name="Month",
    value_name="Forecast Sales"
)

# Plot
fig = px.line(
    plot_df,
    x="Month",
    y="Forecast Sales",
    markers=True,
    title=f"{segment} Forecast"
)

st.plotly_chart(fig, use_container_width=True)
