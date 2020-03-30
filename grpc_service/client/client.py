from . import helpers


def get_all_tweets():
    all_tweets = helpers.get_all_tweets()
    return all_tweets


def get_tweets(username):
    all_tweets = helpers.get_tweets(username)
    return all_tweets


def create_tweet(username, content, tags):
    tweet_new = helpers.create_tweet(username, content, tags)
    return tweet_new


def remove_tweet(tweet_id):
    helpers.remove_tweet(tweet_id)


def edit_tweet(tweet_id, new_content, new_tags):
    helpers.edit_tweet(tweet_id, new_content, new_tags)
