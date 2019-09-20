# The program uses the tweepy for accessing the twitter API 
# Also used textblob to perform actual sentimental analysis.
import tweepy
from textblob import TextBlob

consumer_key = "vEsLsyLWzwrNFS46RHdGsktMj"
consumer_secret = "G05hf1TBUFU8SpbEA8jRdBKHuDEEHR8Lwu17dPEIuD0sk07Vv6"

access_token = "1094978973245812738-Ql5diJug0747TK3td5ncVCwztLMrxI" 
access_token_secret = "NRGCDQccPUMdvtRf35UQzX6SQ9qtwkEdSpLD2mppI4rvU"

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
