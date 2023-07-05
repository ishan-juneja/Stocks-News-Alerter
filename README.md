# Stocks-News-Alerter
This program messages you relevant news of any stock you wish to track that has a 5 percent net change of price from its preceding day.

## Structure
- `main.py` behaves as the nucleus and runs the entirety of the program
  
## Dependencies & Configurations
1. The [Alphavantage API](https://www.alphavantage.co/) to retrieve all the info including the closing and opening price about our desired stock.
   - Retrieve your **STOCK_API_KEY** once you create your account
   - Add to `main.py`
2. The [News API](https://newsapi.org/) to retrieve all the top headline news related to our stock.
   - Retrieve your **NEWS_API_KEY** once you create your account
   - Add to `main.py`
3. The [pandas library](https://pandas.pydata.org/) to make it easier and more efficient to work with our news data

## Demo
The stocks info we enter in `main.py` to track.
<img width="193" alt="Screenshot 2023-07-05 at 9 34 48 AM" src="https://github.com/ishan-juneja/Stocks-News-Alerter/assets/69048541/19c67d3c-fa75-4a11-9177-03e989d858f4">

If there is a net 5 percent change (the program is currently set to ignore its test for testing purposes), then we get a text message with all the relevant news.
