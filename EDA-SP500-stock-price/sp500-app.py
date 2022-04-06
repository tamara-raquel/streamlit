#Importações necessárias:
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yfinance as yf

st.tile('S&P 500 App')

st.markdown("""
Este aplicativo exibe a lista das empresas listadas na S&P500 (web scraping da Wikipedia) e seus correspondentes preços de fechamento (year-to-date).
* **Bibliotecas Python:** base64, pandas, streamlit, numpy, matplotlib, seaborn, yfinance
* **Fonte dos dados:** [Wikipedia](https://www.wikipedia.org/)
""")

st.sidebar.header('User Input Features')

#web scraping dos dados da S&P500
@st.cache
def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url, header=0)
    df = html[0]
    return df