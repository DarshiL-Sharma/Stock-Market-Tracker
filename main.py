import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"      # company name

STOCK_API_KEY ="*******************" # unique key
NEWS_API_KEY = "****************************" # news API key
STOCK_ENDPOINT = "https://www.alphavantage.co/query"  # stock market API
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"  # news article API
TWILIO_SID ="**********************"
TWILIO_AUTH_TOKEN = "***********************" # unique TOKEN ID
MSG_SERVICE_SID= "******************************"
API_PARAMETERS ={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY
}

response  = requests.get(STOCK_ENDPOINT , params=API_PARAMETERS)
data = (response.json()["Time Series Daily"])
print(data)

data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4.close"]
print(yesterday_closing_price)



day_before_yesterday_data = data_list[1]
day_before_yesterday_data_closing_price = day_before_yesterday_data["4.close"]
print(day_before_yesterday_data_closing_price)




difference = round( float(yesterday_closing_price) - float(day_before_yesterday_data_closing_price))
up_down = False
if difference > 0 :
    up_down = "☝️"
else:
    up_down = "👇"



diff_percent = (difference/float(yesterday_closing_price)) * 100
if abs(diff_percent) > 5:
    new_params = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(url=NEWS_ENDPOINT,params=new_params)
    articles = (news_response.json()["articles"])



    three_articles = articles[:3]
    print(three_articles)


    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline : {article['title']}\nBrief : {article['description']}" for article in three_articles]




    client = Client(TWILIO_SID,TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            messaging_service_sid="************************",  # message ID
            body=article,
            to="**************" # your mobile number
        )



