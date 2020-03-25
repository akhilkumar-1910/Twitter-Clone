from database import twitter_clone_db
from google.protobuf.timestamp_pb2 import Timestamp
from proto.twitter_clone_pb2 import Tweet


def get_all_tweets():
    tweets = twitter_clone_db.get_all_tweets()
    t1 = Timestamp()
    t2 = Timestamp()
    all_tweets = []
    for tweet in tweets:
        if tweet.posted_at is not None:
            t1.FromDatetime(tweet.posted_at)
        if tweet.last_edited_at is not None:
            t2.FromDatetime(tweet.last_edited_at)
        else:
            t2 = t1
        ret_tweet = Tweet(
            id=tweet.id,
            username=tweet.username,
            content=tweet.content,
            posted_at=t1,
            last_edited_at=t2,
        )
        for tag in tweet.tags:
            ret_tweet.tag.append(tag.tag)
        all_tweets.append(ret_tweet)
    return all_tweets


def get_tweets(request):
    tweets = twitter_clone_db.get_tweets(request)
    t1 = Timestamp()
    t2 = Timestamp()
    all_tweets = []
    for tweet in tweets:
        if tweet.posted_at is not None:
            t1.FromDatetime(tweet.posted_at)
        if tweet.last_edited_at is not None:
            t2.FromDatetime(tweet.last_edited_at)
        else:
            t2 = t1
        ret_tweet = Tweet(
            id=tweet.id,
            username=tweet.username,
            content=tweet.content,
            posted_at=t1,
            last_edited_at=t2,
        )
        for tag in tweet.tags:
            ret_tweet.tag.append(tag.tag)
        all_tweets.append(ret_tweet)
    return all_tweets


def create_tweet(request):
    twitter_clone_db.create_tweet(request)


def remove_tweet(request):
    twitter_clone_db.remove_tweet(request)


def edit_tweet(request):
    twitter_clone_db.edit_tweet(request)
