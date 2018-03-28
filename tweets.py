import tweepy
from tweepy import OAuthHandler

consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-SECRET'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

#public_tweets = api.user_timeline('realdonaldtrump', tweet_mode='extended')
#print(public_tweets[5].text)

myfile = open('tweets.txt', "w")

# for tweet in public_tweets:
#    myfile.write(tweet.full_text+"\n")

for status in tweepy.Cursor(api.user_timeline, id="realDonaldTrump", tweet_mode='extended', until='2017-03-29').items():
    myfile.write(status.full_text+"\n")

myfile.close()

# Get the User object for twitter...
user = api.get_user('sharmaraghav260')

# print (user.screen_name)
# print (user.followers_count)
# for friend in user.friends():
#    print (friend.screen_name)