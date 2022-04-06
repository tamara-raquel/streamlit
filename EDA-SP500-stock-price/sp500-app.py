# Importações das bibliotecas necessárias:
import streamlit as st #para rodar a aplicacao
import pandas as pd #manipular o dataframe
import base64 #encode dos dados
import matplotlib.pyplot as plt #plotar os graficos
import yfinance as yf #dados financeiros das empresas

# ----- Parte I - Dados de Cadastro -----

st.title('S&P 500 App')

st.markdown("""
Este aplicativo exibe a lista das empresas listadas na S&P500 (web scraping da Wikipedia) e seus correspondentes preços de fechamento (year-to-date).
* **Bibliotecas Python:** base64, pandas, streamlit, matplotlib, yfinance
* **Fonte dos dados:** [Wikipedia](https://www.wikipedia.org/)
""")

# Barra lateral com as funcionalidades que o usuário pode escolher
st.sidebar.header('Recursos do usuário')

# Web scraping dos dados da S&P500
# Fonte: Página web da Wikipedia
# Funcao customizada para pegar os dados - ver mais detalhes no notebook que consta no diretório
@st.cache
def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url, header=0)
    df = html[0]
    return df

# Agrupando empresas por setor
df = load_data()
sector = df.groupby('GICS Sector')

# Sidebar - selecao do setor
sorted_sector_unique = sorted(df['GICS Sector'].unique())
# Permite a seleção de mais de um setor:
selected_sector = st.sidebar.multiselect('Sector', sorted_sector_unique, sorted_sector_unique)

# Filtrando os dados
df_selected_sector = df[(df['GICS Sector'].isin(selected_sector))]

# Exibe dados das empresas selecionadas nos 3 setores
st.header('Display Companies in Selected Sector')
# Dá as dimensões: exibe numero de linhas e colunas
st.write('Data Dimension: ' + str(df_selected_sector.shape[0]) + ' rows and ' + str(df_selected_sector.shape[1]) + ' columns.')
st.dataframe(df_selected_sector)

# Download S&P500 data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806

# Funcao customizada para encode/decode dos dados
# Permite o download dos dados filtrados, no formato CSV
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_sector), unsafe_allow_html=True)

# ----- Parte II - Dados Financeiros -----

# Fonte: Bilioteca do Yahoo Financas
# https://pypi.org/project/yfinance/
# Ver mais detalhes sobre a funcao seguinte no notebook
data = yf.download(
        tickers = list(df_selected_sector[:10].Symbol),
        period = "ytd",
        interval = "1d",
        group_by = 'ticker',
        auto_adjust = True,
        prepost = True,
        threads = True,
        proxy = None
    )

# Configuraçoes basicas de plotagem dos graficos
def price_plot(symbol):
  df = pd.DataFrame(data[symbol].Close)
  df['Date'] = df.index
  plt.fill_between(df.Date, df.Close, color='skyblue', alpha=0.3)
  plt.plot(df.Date, df.Close, color='skyblue', alpha=0.8)
  plt.xticks(rotation=90)
  plt.title(symbol, fontweight='bold')
  plt.xlabel('Date', fontweight='bold')
  plt.ylabel('Closing Price', fontweight='bold')
  return st.pyplot()

# Slider para selecionar o numero de empresas que devem ser gerados os graficos
# Limites determinados: min 1 e max 5
num_company = st.sidebar.slider('Number of Companies', 1, 5)

if st.button('Show Plots'):
    st.header('Stock Closing Price')
    for i in list(df_selected_sector.Symbol)[:num_company]:
        price_plot(i)


# ----- Parte III - Rodando a aplicação com o Streamlit -----

# Abra o cmd
# Navegue até o diretório em que se encontra o arquivo sp500-app.py
# Na linha de comando: streamlit run sp500-app.py
# Uma página no navegador em local:host será aberta para exibir o aplicativo