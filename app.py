import streamlit aas st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(page_title = "Stock Data Extraction App", layout = "wide")
st.title("Stock Data Extraction App")
st.write("Extract Stock Market Data from Yahoo Finance using ticker symbol")
st.sidebar.header("Options")
ticker = st.sidebar.text_input("Ticker Symbol", "AAPL")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))
# Download the "data button"

if st.sidebar.button("Get Data"):
  # ticker object
  stock = yf.Ticker(ticker)

  # Download historical price date
  df = stock.history(start = start_date, end = end_date)

  #Check the data
  if df.empty:
    st.error("No data available for the selected date range.")
  else:
    # Show success message
    st.success(f"Data successfully extracted for {ticker}")
    # Display Company Information
    st.subheader("Company Information")
    info = stock.info

    company_name = info.get("longName", "N/A")
    sector = info.get("sector","N/A")
    industry = info.get("industry","N/A")
    market_cap = info.get("marketCap", "N/A")
    website = info.get("website","N/A")

    st.write(f"Company Name: {company_name}")
    st.write(f"Sector: {sector}")
    st.write(f"Industry: {industry}")
    st.write(f"Market Cap: {market_cap}")
    st.write(f"Website: {website}")

    # Display stock data
    st.subheader("Historical Stock Data")
    st.datafram(df)

    # Plot Closing Price
    st.subheader("Closing Price Chart")
    fig, ax = plt.subplots()
    ax.plot(df.index, df["Close"])
    ax.set_xlabel("Date")
    ax.set_ylabel("Closing Price")
    ax.title(f"{ticker} Closing Price")
    st.pyplot(fig)

    # Convert dataframe to CSV file so it can be downloaded
    csv = df.to_csv().encode("utf-8")
    
    # Download Button
    st.download_button(
        label = "Download Data as CSV",
        data = csv,
        file_name = f"{ticker}_stock_data.csv",
        mime = "text/csv"
    )
