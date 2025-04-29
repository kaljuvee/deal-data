import streamlit as st

st.set_page_config(
    page_title="Deal Data Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("Deal Data Analytics Dashboard")
st.markdown("""
### Welcome to the Deal Data Analytics Dashboard

This application provides comprehensive data analysis for deal evaluation by integrating multiple data sources:

1. **Yahoo Finance API**
   - Financial metrics and company information
   - Enterprise value and market data
   - Public company comparables
   - Regulatory filings

2. **Bing Search API**
   - Project and investment information
   - Economic indicators
   - Political and market analysis
   - Stakeholder information

3. **Bing News API**
   - Latest company news
   - Market sentiment analysis
   - Competitor information
   - Regulatory updates

### How to Use
1. Navigate to any of the API pages using the sidebar
2. Enter a company name or ticker symbol
3. Click "Get Data" to retrieve and analyze information
4. View the results in the interactive tables and news feeds

### Data Coverage
The application covers key metrics including:
- Project size and investment details
- Economic indicators
- Political and market stability
- News and sentiment analysis
- Competitor information
- Regulatory compliance

""")

# Add navigation to other pages
st.sidebar.title("Navigation")
st.sidebar.markdown("""
- [Yahoo Finance API](/Yahoo_Finance_API)
- [Bing Search API](/Bing_Search_API)
- [Bing News API](/Bing_News_API)
""")
