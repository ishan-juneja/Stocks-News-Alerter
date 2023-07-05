import requests
import pandas as pd
import os
from twilio.rest import Client
STOCK = "GOOGL"
COMPANY_NAME = "Google"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.environ["STOCK_API_KEY"]
NEWS_API_KEY = os.environ["NEWS_API_KEY"]


# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
keyload = {"function":"TIME_SERIES_DAILY_ADJUSTED", "symbol":STOCK,"outputsize":"compact", "apikey":STOCK_API_KEY}
response = requests.get("https://www.alphavantage.co/query?", params=keyload)
stock_csv = response.json()
print(response.status_code)

#creating an iter object letting us iterate through the stock items as tuples
#access the specific values in the tuples
iter_stocks = iter(stock_csv['Time Series (Daily)'].items())
open_price = float(next(iter_stocks)[1]['1. open'])
close_price = float(next(iter_stocks)[1]['4. close'])

#checking if there is a 5 percent change

change_percent = open_price/close_price
check_news = False
if(close_price * 0.05 <= abs(open_price-close_price)):
    check_news = True
check_news = True
print(check_news)



# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
keyload2 = {"q":f"{STOCK}", "apiKey":NEWS_API_KEY, "pageSize": 3}

response = requests.get("https://newsapi.org/v2/top-headlines?", params=keyload2)
news_json = response.json()
df = pd.DataFrame.from_dict(news_json)
news_list = []
for i, j in df.iterrows():
    news_list.append(j.get("articles"))


# Send a separate message with each article's title and description to your phone number.
text = f"{STOCK}: {round(change_percent,3)}%\n\n"
for article in news_list:
    text = text + "Headline: " + article['title'] + "\nBrief: " + article["description"] + "\n\n"


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=text,
                     from_='+18777647140',
                     to=os.environ["MY_NUMBER"]
                 )


print(message.sid)


