import streamlit as st
import asyncio
import os
from quant_agent import get_analysis

# Load key for the OpenAI SDK
if "OPENAI_API_KEY" in st.secrets:
    os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.title("Quant Agent")
ticker = st.text_input("Ticker", placeholder="AAPL")

if st.button("Run", disabled=not ticker):
    with st.spinner("Analyzing..."):
        st.markdown(asyncio.run(get_analysis(ticker.upper())))
