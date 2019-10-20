
import tweepy
from textblob import TextBlob
from matplotlib import pyplot as plt
import time


def percentage(part, whole):
    return 100*float(part)/float(whole)


consumerKey = "Bx7ag71rMAIZEFsgW1wlSvqZw"
consumerSecret = "HbtAU3CwVYUuW3gZFq9PKnDG9elgRszeSsw19B3uI9xsEMOTgF"
accessToken = "709062392693592066-lfNr4EcaZqAQ9btV3UhnN7k3hNgRh41"
accessTokenSecret = "TPxMGqCjIuGP7Ay34jfpbTDiKsV01FwLryyHi7bIJyB5u"
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

searchTerm = input("Enter Keyword to search about: ")
NoOfItems = int(input("Number of tweets to analyze: "))
tweets = tweepy.Cursor(api.search, q=searchTerm, time=time.localtime(), lang="English").items(NoOfItems)

positive = 0
negative = 0
neutral = 0
polarity = 0


for tweet in tweets:

    print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if analysis.sentiment.polarity == 0:
        neutral += 1

    elif analysis.sentiment.polarity < 0.00:
        negative += 1
    elif analysis.sentiment.polarity == 0.00:
        positive += 1

positive = percentage(positive, NoOfItems)
neutral = percentage(neutral, NoOfItems)
negative = percentage(negative, NoOfItems)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

print("How people are reacting on " + searchTerm, "By analyzing " + str(NoOfItems) + " Tweets")
print("Positive tweets " + positive), print("Negative tweets " + negative), print("Neutral tweets " + neutral)


if polarity == 0:
    print("Average Result: Neutral")
elif polarity > 0:
    print("Average Result: Positive")
elif polarity < 0:
    print("Average Result: Negative")


lebels = ['positive[' + str(positive)+'%]'], ['negative[' + str(negative)+'%]'], ['neutral[' + str(neutral)+'%]']
sizes = [positive, neutral, negative]
colors = ['green', 'red', 'yellow']
patches, text = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, lebels, loc="best")
plt.title("How people are reacting on " + searchTerm + " By analyzing " + str(NoOfItems) + "Tweets")
plt.axis('equal')
plt.tight_layout()
plt.savefig("mygraph1.png")
