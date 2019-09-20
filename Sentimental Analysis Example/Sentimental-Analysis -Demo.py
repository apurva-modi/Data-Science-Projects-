# Used textblob to perform actual sentimental analysis.
from textblob import TextBlob

string_input = input("Enter the A string for sentimental analysis ")

wiki = TextBlob( string_input )

print(wiki.tags)
print(wiki.sentiment)
print(wiki.sentiment.polarity) #Gives the polarity between -1 to +1
