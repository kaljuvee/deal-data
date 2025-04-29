import streamlit as st
import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()

st.title("Bing Search API Integration")

# Text input for company name
company_name = st.text_input("Enter Company Name", value="Microsoft")

if st.button("Get Data"):
    try:
        # Note: You'll need to set BING_SEARCH_KEY in your environment variables
        subscription_key = os.getenv("BING_SEARCH_KEY")
        search_url = "https://api.bing.microsoft.com/v7.0/search"
        
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        params = {"q": company_name, "textDecorations": True, "textFormat": "HTML"}
        
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        
        # Create a DataFrame with the relevant metrics
        data = {
            'Metric': [
                'Project size',
                'Project Compass (Energy Co)',
                'Investment size',
                'Population',
                'GDP',
                'GDP per capita',
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
                'Competitor Deals',
                'Advisors/Vendors'
            ],
            'Value': [
                'Available through Bing Search API',
                'Available through Bing Search API',
                'Available through Bing Search API',
                'Available through Bing Search API',
                'Available through Bing Search API',
                'Available through Bing Search API',
                'Available through Bing Search API',
                'Available through Bing Search API',
                'Available through Bing Search API',
                'Available through Bing Search API',
                'Available through Bing Search API',
                'Available through Bing Search API',
                'Available through Bing Search API',
                'Available through Bing Search API',
                'Available through Bing Search API',
                'Available through Bing Search API',
                'Available through Bing Search API',
                'Available through Bing Search API',
                'Available through Bing Search API',
                'Available through Bing Search API',
                'Available through Bing Search API'
            ],
            'Source': ['Bing Search API'] * 21
        }
        
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
        
        # Display search results
        st.subheader("Search Results")
        for result in search_results.get("webPages", {}).get("value", [])[:5]:
            st.write(f"**{result['name']}**")
            st.write(result['snippet'])
            st.write(f"[Read more]({result['url']})")
            st.write("---")
            
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}") 