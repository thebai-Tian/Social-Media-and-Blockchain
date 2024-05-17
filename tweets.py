import tweepy


auth = tweepy.OAuth1UserHandler(
    consumer_key="*",
    consumer_secret="*",
    access_token="*",
    access_token_secret="*"
)
api = tweepy.API(auth)


query = "Dogecoin OR $DOGE"
since_timestamp = 1702666221  
until_timestamp = 1703022954  


tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en", since_id=since_timestamp, until_id=until_timestamp).items()
tweet_data = [[tweet.created_at, tweet.text, tweet.favorite_count, tweet.retweet_count] for tweet in tweets]

for data in tweet_data:
    print(data)
