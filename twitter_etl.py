import tweepy

def post_tweet(message):
    bearer_token = '[bearer_token]'
    consumer_key = '[key]'
    consumer_secret = '[secret]'
    access_token = '[access_token]'
    access_token_secret = '[access_secret]'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(message)
