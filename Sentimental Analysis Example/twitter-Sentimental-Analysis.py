# The program uses the tweepy for accessing the twitter API 
# Also used textblob to perform actual sentimental analysis.
import tweepy
from textblob import TextBlob

consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET_KEY"

access_token = "YOUR_ACCESS_TOKEN" 
access_token_secret = "YOUR_TOKEN_SECRET_KEY"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("Trump")

for tweets in public_tweets:
    print(tweets.text)
    analysis = TextBlob(tweets.text)
    #Polarity measures how positive and negative a tweet is.
    #Subjectivity measures how much an opinion it is and factual it is.
    print(analysis.sentiment)
