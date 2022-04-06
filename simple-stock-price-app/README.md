# simple stock price app
*App utilizando streamlit e python*

Este app plota gráficos do preço de fechamento e volume por ação.

## Para rodar a aplicação:

cmd: streamlit run simple-stock-price-app.py

Uma página será aberta no navegador para exibir o app. 

O app permite zoom in, zoom out e outras movimentações para facilitar a visualização de um determinado período. Para voltar ao estado inicial, clique duplo no gráfico.

### É necessário:

 - ter o streamlit instalado [pip install streamlit]
 - ter a biblioteca yfinance instalada

## Mais sobre a aplicação:

Neste exemplo, são mostrados os resultados para o ticker GOOGL, da empresa Google.

Para exibir os resultados para outras empresas, basta trocar o ticker.

Além da opções de gráfico demonstradas, é possível também mostrar resultados para preço de abertura, o mais alto, mais baixo, dividendos, etc.

Para isso usar tickerOf. [Open/High/Low/Dividends...]
