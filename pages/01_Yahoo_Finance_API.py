import streamlit as st
import yfinance as yf
import pandas as pd
import time

st.title("Yahoo Finance API Integration")

# Add rate limiting
@st.cache_data(ttl=300)  # Cache for 5 minutes
def get_company_info(ticker):
    try:
        company = yf.Ticker(ticker)
        # Add a small delay to prevent rate limiting
        time.sleep(1)
        return company.info
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}")
        return None

# Text input for ticker/company name
ticker = st.text_input("Enter Ticker Symbol or Company Name", value="AAPL")

if st.button("Get Data"):
    try:
        # Get company info with rate limiting
        info = get_company_info(ticker)
        
        if info is None:
            st.warning("Please wait a few seconds before trying again.")
        else:
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
            
            # Add a cooldown message
            st.info("Please wait at least 5 seconds before making another request to avoid rate limiting.")
        
    except Exception as e:
        st.error(f"Error processing data: {str(e)}")
        st.info("If you're seeing rate limit errors, please wait a few minutes before trying again.") 