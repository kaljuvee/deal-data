import streamlit as st
import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()

st.title("Bing News API Integration")

# Text input for company name
company_name = st.text_input("Enter Company Name", value="Microsoft")

if st.button("Get Data"):
    try:
        # Note: You'll need to set BING_NEWS_KEY in your environment variables
        subscription_key = os.getenv("BING_NEWS_KEY")
        search_url = "https://api.bing.microsoft.com/v7.0/news/search"
        
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        params = {"q": company_name, "textDecorations": True, "textFormat": "HTML"}
        
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        
        # Create a DataFrame with the relevant metrics
        data = {
            'Metric': [
                'Project Compass (Energy Co)',
                'Investment size',
                'BOEPD',
                'BOE',
                'Equity investment',
                'Population',
                'GDP',
                'GDP per capita',
                'FX (against $)',
                'Sovereign credit rating',
                'Debt to GDP',
                'Inflation rate',
                'Political stability',
                'Political exposure',
                'Emissions intensity',
                'Target Company News',
                'Sector Analysis News',
                'Market Sentiment',
                'Competitor News',
                'Geopolitcal News',
                'Regulatory News',
                'Connected stakeholders',
                'Competitor Deals'
            ],
            'Value': [
                'Available through Bing News API',
                'Available through Bing News API',
                'Available through Bing News API',
                'Available through Bing News API',
                'Available through Bing News API',
                'Available through Bing News API',
                'Available through Bing News API',
                'Available through Bing News API',
                'Available through Bing News API',
                'Available through Bing News API',
                'Available through Bing News API',
                'Available through Bing News API',
                'Available through Bing News API',
                'Available through Bing News API',
                'Available through Bing News API',
                'Available through Bing News API',
                'Available through Bing News API',
                'Available through Bing News API',
                'Available through Bing News API',
                'Available through Bing News API',
                'Available through Bing News API',
                'Available through Bing News API',
                'Available through Bing News API'
            ],
            'Source': ['Bing News API'] * 23
        }
        
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
        
        # Display news results
        st.subheader("News Results")
        for article in search_results.get("value", [])[:5]:
            st.write(f"**{article['name']}**")
            st.write(article['description'])
            st.write(f"Published: {article.get('datePublished', 'N/A')}")
            st.write(f"[Read more]({article['url']})")
            st.write("---")
            
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}") 