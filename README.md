# Deal Data Analytics Dashboard

A comprehensive data analysis tool for deal evaluation that integrates multiple data sources including Yahoo Finance, Bing Search, and Bing News APIs.

## Features

- **Yahoo Finance Integration**
  - Financial metrics and company information
  - Enterprise value and market data
  - Public company comparables
  - Regulatory filings

- **Bing Search Integration**
  - Project and investment information
  - Economic indicators
  - Political and market analysis
  - Stakeholder information

- **Bing News Integration**
  - Latest company news
  - Market sentiment analysis
  - Competitor information
  - Regulatory updates

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/deal-data.git
   cd deal-data
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with your API keys:
   ```
   BING_SEARCH_KEY=your_bing_search_api_key
   BING_NEWS_KEY=your_bing_news_api_key
   ```

   Note: Yahoo Finance API doesn't require an API key.

## Usage

1. Start the Streamlit app:
   ```bash
   streamlit run Home.py
   ```

2. Navigate to the desired API page using the sidebar:
   - Yahoo Finance API
   - Bing Search API
   - Bing News API

3. Enter a company name or ticker symbol and click "Get Data" to retrieve information.

## Requirements

- Python 3.7+
- Streamlit
- Pandas
- yfinance
- requests
- python-dotenv

## API Keys

To use the Bing APIs, you'll need to:
1. Create a Microsoft Azure account
2. Subscribe to Bing Search and News APIs
3. Get your API keys from the Azure portal
4. Add them to your `.env` file

## Contributing

Feel free to submit issues and enhancement requests!