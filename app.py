import streamlit as st
import yfinance as yf
import datetime
st.write("""
         # Stock Price Prediction
         """)


symbol = st.selectbox(
    'Which Stock Symbol would you want to select',
    ('AAPL','GOOG','TSLA','MSFT','AMZN','META','GS','NKE','WMT'))
col1,col2 = st.columns(2)
with col1:
    start_data = st.date_input("Please Enter Start Date",datetime.date(2019,7,6))
with col2:
    end_date = st.date_input("Enter End Date",datetime.date(2019,7,10))


ticker_data = yf.Ticker(symbol)
ticker_df = ticker_data.history(period="1d",start=start_data,end=end_date)


st.write(f"""
       ### {symbol}'s Stock Price Data
         """)
st.dataframe(ticker_df)



st.write(f"""
### {symbol}'s Closing Charts
         """)
st.line_chart(ticker_df["Close"])


st.write(f"""
### {symbol}'s Volume Charts
         """)
st.line_chart(ticker_df["Volume"])


st.write(f"""
### {symbol}'s Close Charts
         """)
st.area_chart(ticker_df["Close"])


st.write(f"""
### {symbol}'s Volume Charts
         """)
st.area_chart(ticker_df["Volume"])

st.write(f"""
### {symbol}'s Close Charts
         """)
st.bar_chart(ticker_df["Close"])

st.write(f"""
### {symbol}'s Volume Charts
         """)
st.bar_chart(ticker_df["Volume"])
