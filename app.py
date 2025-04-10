
import streamlit as st
import pandas as pd
import plotly.io as pio

st.set_page_config(layout="wide")

# Title
st.title("Fantasy Football AI Cheat Sheet")

# Introduction
st.write("Welcome to my AI-powered fantasy football cheat sheet. This includes my AI-generated rankings, graphs, and a detailed report.")

# Display Cheat Sheet
st.subheader("📊 Cheat Sheet")
final_cheat_sheet = pd.read_csv("cheat_sheet.csv")
st.dataframe(final_cheat_sheet)

# Display Graphs
st.subheader("📈 Interactive Graph")
fig2 = pio.read_json("fig2.json")
st.plotly_chart(fig2)

# Link to AI Report
st.subheader("📜 AI Report")
report_link = "https://docs.google.com/document/d/1RrfK8E6011Zv7yUY0A1m8onGyKgPZlFVSQH5RPzDv8k/edit?usp=sharing"
st.markdown(f"[View Full Report on Google Docs]({report_link})")

st.subheader("📜 Code Breakdown")
report_link = "https://docs.google.com/presentation/d/1qizWfV1B1CJzF6_KA0qAXHtVL_DH6kXVqQgf41DnvzE"
st.markdown(f"[View Full Report on Google Docs]({report_link})")

st.subheader("📜 Documentation")
report_link = "https://docs.google.com/document/d/1aIg41c8-Er_v6YZQZLjuL_m4pHcvxRDrxF0itna-qVw"
st.markdown(f"[View Full Report on Google Docs]({report_link})")

# Footer
st.write("Made by Anay")
