import streamlit as st
import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()

st.title("Bing Search API Integration")

# Define available metrics
METRICS = [
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
]

# Text input for company name
company_name = st.text_input("Enter Company Name", value="Microsoft")

# Metric selection dropdown
selected_metric = st.selectbox("Select Metric to Search", METRICS)

if st.button("Get Data"):
    try:
        # Note: You'll need to set BING_SEARCH_KEY in your environment variables
        subscription_key = os.getenv("BING_SEARCH_KEY")
        search_url = "https://api.bing.microsoft.com/v7.0/search"
        
        # Create search query combining company name and selected metric
        search_query = f"{company_name} {selected_metric}"
        
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        params = {"q": search_query, "textDecorations": True, "textFormat": "HTML"}
        
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        
        # Create a DataFrame with the search results
        results_data = []
        for result in search_results.get("webPages", {}).get("value", [])[:5]:
            results_data.append({
                'Metric': selected_metric,
                'Result': result['snippet'],
                'Source': result['url']
            })
        
        df = pd.DataFrame(results_data)
        st.dataframe(df, use_container_width=True)
        
        # Display detailed search results
        st.subheader("Detailed Search Results")
        for result in search_results.get("webPages", {}).get("value", [])[:5]:
            st.write(f"**{result['name']}**")
            st.write(result['snippet'])
            st.write(f"[Read more]({result['url']})")
            st.write("---")
            
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}") 