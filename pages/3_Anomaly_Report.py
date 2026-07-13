
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Anomaly Detection Report")

anomaly_df = pd.DataFrame({
    "Date":[
        "2017-11-26",
        "2017-12-03",
        "2016-01-10"
    ],
    "Sales":[
        32000,
        34000,
        1200
    ]
})

fig, ax = plt.subplots()

ax.plot(
    anomaly_df["Date"],
    anomaly_df["Sales"]
)

ax.scatter(
    anomaly_df["Date"],
    anomaly_df["Sales"],
    color="red"
)

st.pyplot(fig)

st.dataframe(anomaly_df)
