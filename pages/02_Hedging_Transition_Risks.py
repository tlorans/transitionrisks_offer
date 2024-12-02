import streamlit as st
import yfinance as yf

st.title('Hedging Transition Risks')



etfs = {
    "IWRD.L": "iShares MSCI World UCITS ETF",
    "SPY" : "SPDR S&P 500 ETF Trust",
        "EEM" : "iShares MSCI Emerging Markets ETF",
        "IWM" : "iShares Russell 2000 ETF"
}

list_tickers = list(etfs.values())

name_etf = st.sidebar.selectbox('Select ETF', list_tickers)

# find the corresponding key
ticker = [key for key, value in etfs.items() if value == name_etf][0]

prices = (yf.download(
    tickers=ticker, 
    progress=False
  )
  .reset_index()
  .assign(name = lambda x: name_etf)
  .rename(columns={
      "Date": "date",
    "Open": "open",
    "High": "high",
    "Low": "low",
    "Close": "close",
    "Adj Close": "adjusted",
    "Volume": "volume"
  })
  )

st.write(prices)