import os, praw, tweepy

'''Twitter Authentication'''
CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]
auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
history_api = tweepy.API(auth, wait_on_rate_limit=True)

'''Reddit Authentication'''
reddit_read_only = praw.Reddit(
    user_agent=os.environ["user_agent1"],
    client_id=os.environ["client_id1"],
    client_secret=os.environ["client_secret1"],
)
subreddit = reddit_read_only.subreddit("HistoryMemes")
post_dict = {}