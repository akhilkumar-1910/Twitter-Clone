from . import twitter_clone_stub


def get_all_tweets():
    tweets = twitter_clone_stub.get_all_tweets()
    all_tweets = [
        {
            "id": tweet.id,
            "username": tweet.username,
            "content": tweet.content,
            "posted_at": tweet.posted_at.ToDatetime(),
            "last_edited_at": tweet.last_edited_at.ToDatetime(),
            "tags": tweet.tag,
        }
        for tweet in tweets
    ]
    return all_tweets


def get_tweets(username):
    tweets = twitter_clone_stub.get_tweets(username)
    all_tweets = [
        {
            "id": tweet.id,
            "username": tweet.username,
            "content": tweet.content,
            "posted_at": tweet.posted_at.ToDatetime(),
            "last_edited_at": tweet.last_edited_at.ToDatetime(),
            "tags": tweet.tag,
        }
        for tweet in tweets
    ]
    return all_tweets


def create_tweet(username, content, tags):
    tweet = twitter_clone_stub.create_tweet(username, content, tags)
    tweet_new = {
        "username": tweet.username,
        "content": tweet.content,
        "posted_at": tweet.posted_at,
        "last_edited_at": tweet.last_edited_at,
        "tags": tweet.tag,
    }
    return tweet_new


def remove_tweet(tweet_id):
    twitter_clone_stub.remove_tweet(tweet_id)


def edit_tweet(tweet_id, new_content, new_tags):
    twitter_clone_stub.edit_tweet(tweet_id, new_content, new_tags)
