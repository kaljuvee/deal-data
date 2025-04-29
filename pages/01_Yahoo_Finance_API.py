import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Yahoo Finance API Integration")

# Text input for ticker/company name
ticker = st.text_input("Enter Ticker Symbol or Company Name", value="AAPL")

if st.button("Get Data"):
    try:
        # Get company info
        company = yf.Ticker(ticker)
        info = company.info
        
        # Create a DataFrame with the relevant metrics
        data = {
            'Metric': [
                'Enterprise Value (EV)',
                'FX (against $)',
                'Ticker information',
                'Public company comparables',
                'O&G/Commodity Pricing',
                'Company regulatory filings'
            ],
            'Value': [
                f"${info.get('enterpriseValue', 'N/A')}",
                info.get('currency', 'N/A'),
                f"{ticker} - {info.get('longName', 'N/A')}",
                'Available through Yahoo Finance API',
                'Available through Yahoo Finance API',
                'Available through Yahoo Finance API'
            ],
            'Source': ['Yahoo Finance API'] * 6
        }
        
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
        
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}") 