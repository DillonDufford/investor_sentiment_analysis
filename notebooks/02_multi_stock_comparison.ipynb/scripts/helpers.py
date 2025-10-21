
import requests
import pandas as pd
from bs4 import BeautifulSoup
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# ----------------------------
# Function to scrape news
# ----------------------------
def scrape_news(ticker, max_articles=50):
    # Example structure; adapt as needed
    all_news = []
    # scraping logic here...
    return all_news

# ----------------------------
# Function to get sentiment from text
# ----------------------------
def get_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)['compound']

# ----------------------------
# Function to get sentiment from news list
# ----------------------------
def get_news_sentiment(news_list):
    sentiment_scores = [get_sentiment(article) for article in news_list]
    return sum(sentiment_scores)/len(sentiment_scores) if sentiment_scores else 0

# ----------------------------
# Function to plot stock trends
# ----------------------------
def plot_stock_trends(df, ticker):
    fig, ax = plt.subplots(figsize=(12,5))
    ax.plot(df['Date'], df['Close'], label='Close Price')
    ax.set_title(f"{ticker} Close Price Trend")
    ax.set_xlabel('Date')
    ax.set_ylabel('Close Price')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
