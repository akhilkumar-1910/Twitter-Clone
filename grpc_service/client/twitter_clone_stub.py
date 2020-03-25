from grpc_service.proto.twitter_clone_pb2 import Tweet


def get_all_tweets(stub):
    tweet = Tweet()
    tweets = stub.GetAllTweets(tweet)
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


def get_tweets(stub, username):
    tweet = Tweet(username=username)
    tweets = stub.GetTweets(tweet)
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


def create_tweet(stub, username, content, tags):
    tweet = Tweet(
        username=username,
        content=content,
    )
    for tag in tags:
        tweet.tag.append(tag)
    tweet = stub.CreateTweet(tweet)
    tweet_new = {
        "username": tweet.username,
        "content": tweet.content,
        "posted_at": tweet.posted_at,
        "last_edited_at": tweet.last_edited_at,
        "tags": tweet.tag,
    }
    return tweet_new


def remove_tweet(stub, tweet_id):
    tweet = Tweet(
        id=tweet_id
    )
    stub.RemoveTweet(tweet)


def edit_tweet(stub, tweet_id, new_content, new_tags):
    tweet = Tweet(
        id=tweet_id,
        content=new_content,
    )
    for tag in new_tags:
        tweet.tag.append(tag)
    stub.EditTweet(tweet)
