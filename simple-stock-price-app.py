import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App


Shown are the stock closing price and volume of Google!

""")

#define the ticker symbol
tickerSymbol = 'GOOGL'

#get the data in this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for the ticker
tickerOf = tickerData.history(period='1d', start='2011-5-31', end='2021-5-31')

st.line_chart(tickerOf.Close)
st.line_chart(tickerOf.Volume)