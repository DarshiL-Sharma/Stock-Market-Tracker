# Stock-Market-Tracker
A smart stock monitoring app that tracks real-time price changes and detects variations above 2%. When triggered, it automatically sends SMS alerts with the latest company news using APIs. Stay updated instantly with important market movements. 🚀📊

🚀 Features

-📊 Tracks real-time stock prices
-📉 Detects price variation above 2%
-📰 Fetches latest company-related news
-📲 Sends instant SMS alerts
-⚡ Fully automated monitoring system
-📰 Fetches latest company news articles
-📲 Sends detailed SMS alerts (price + news)

🛠️ Built With

-🐍 Python
-🌐 requests (for API calls)
-📩 Twilio (for SMS alerts)

🔧 How It Works
1.Fetches stock price data using an API.
2.Calculates percentage change.
3.If change > 5%, fetches latest news articles.
4.Send's SMS notification with price update + news via Twilio.
5.Send formatted SMS including:
Price direction (🔺/🔻)
Percentage change

Top 3 news headlines + brief descriptions
