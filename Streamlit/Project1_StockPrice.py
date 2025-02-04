import yfinance as yf
import streamlit as st
import pandas as pd
import datetime

st.write(
    """
      # Simple Stock Price App
      
    """
)
tickerSym=["AAPL","GOOGL","MSFT","AMZN"]
select_ticker_sym=st.sidebar.selectbox("Select Ticker Symbol",tickerSym)

tickerData=yf.Ticker(select_ticker_sym)
tickerchart=["Open","High","Close","Low","Volume","Dividends","Stock Splits"]
selectchart=st.sidebar.selectbox("Select Chart",tickerchart)
startdate=st.sidebar.date_input("Start Date",datetime.date(2008,1,1))
enddate=st.sidebar.date_input("End Date",datetime.date.today())

sentense="Displayed is the **{}** Price Of **{}**".format(selectchart,select_ticker_sym)
st.markdown(sentense)
tickerDf=tickerData.history(period='1d',start=startdate,end=enddate)

st.line_chart(tickerDf[selectchart])


