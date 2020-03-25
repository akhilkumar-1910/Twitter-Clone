from . import twitter_clone_stub


def get_all_tweets(stub):
    return twitter_clone_stub.get_all_tweets(stub)


def get_tweets(stub, username):
    return twitter_clone_stub.get_tweets(stub, username)


def create_tweet(stub, username, content, tags):
    return twitter_clone_stub.create_tweet(stub, username, content, tags)


def remove_tweet(stub, tweet_id):
    twitter_clone_stub.remove_tweet(stub, tweet_id)


def edit_tweet(stub, tweet_id, new_content, new_tags):
    twitter_clone_stub.edit_tweet(stub, tweet_id, new_content, new_tags)
