import tweepy
import time

consumer_key, consumer_secret = '', ''
access_token, access_token_secret = '', ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name)
print(user.description)
print(user.location)
print (user.followers_count)

search = 'thalapathy'
numberOfTweets = 5

# To resrict the api call for a few seconds, in case of RateLimitError Exception. 
def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(1000)

# To follow or unfollow a certain user 
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
  if follower.name == 'actorvijay':
    print(follower.name)
    # follower.unfollow()
    follower.follow() 
   
# To like certain tweet or retweet anything with a keyword specified!
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite() 
        print('Liked the tweet')
        # tweet.retweet()
        # print('Retweeted')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break    