import streamlit as st
import asyncio
import os
from quant_agent import get_analysis

st.title("Quant Agent")
ticker = st.text_input("Ticker", placeholder="AAPL")

if st.button("Run", disabled=not ticker):
    with st.spinner("Analyzing..."):
        st.markdown(asyncio.run(get_analysis(ticker.upper())))
