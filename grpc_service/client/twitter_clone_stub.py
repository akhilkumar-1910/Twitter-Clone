import grpc
from grpc_service.proto.twitter_clone_pb2 import Tweet
from grpc_service.proto import twitter_clone_pb2_grpc


def get_all_tweets():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = twitter_clone_pb2_grpc.TweetServiceStub(channel)
        tweet = Tweet()
        tweets = stub.GetAllTweets(tweet)
        all_tweets = [tweet for tweet in tweets]
        return all_tweets


def get_tweets(username):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = twitter_clone_pb2_grpc.TweetServiceStub(channel)
        tweet = Tweet(username=username)
        tweets = stub.GetTweets(tweet)
        all_tweets = [tweet for tweet in tweets]
        return all_tweets


def create_tweet(username, content, tags):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = twitter_clone_pb2_grpc.TweetServiceStub(channel)
        tweet = Tweet(
            username=username,
            content=content,
        )
        for tag in tags:
            tweet.tag.append(tag)
        tweet_new = stub.CreateTweet(tweet)
        return tweet_new


def remove_tweet(tweet_id):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = twitter_clone_pb2_grpc.TweetServiceStub(channel)
        tweet = Tweet(
            id=tweet_id
        )
        stub.RemoveTweet(tweet)


def edit_tweet(tweet_id, new_content, new_tags):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = twitter_clone_pb2_grpc.TweetServiceStub(channel)
        tweet = Tweet(
            id=tweet_id,
            content=new_content,
        )
        for tag in new_tags:
            tweet.tag.append(tag)
        stub.EditTweet(tweet)
