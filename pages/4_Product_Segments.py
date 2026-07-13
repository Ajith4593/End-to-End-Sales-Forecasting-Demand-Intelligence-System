
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Product Demand Segments")

cluster_df = pd.DataFrame({

    "Sub-Category":[
        "Phones",
        "Chairs",
        "Tables",
        "Storage",
        "Binders"
    ],

    "Cluster":[
        "Growing Demand",
        "High Volume Stable Demand",
        "Declining Demand",
        "Low Volume High Volatility",
        "Growing Demand"
    ],

    "X":[1,2,3,4,5],
    "Y":[5,4,3,2,1]
})

fig = px.scatter(
    cluster_df,
    x="X",
    y="Y",
    color="Cluster",
    hover_data=["Sub-Category"]
)

st.plotly_chart(fig)

st.dataframe(
    cluster_df[
        ["Sub-Category","Cluster"]
    ]
)
