from . import helpers
import grpc
from grpc_service.proto import twitter_clone_pb2_grpc


def get_all_tweets():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = twitter_clone_pb2_grpc.TweetServiceStub(channel)
        all_tweets = helpers.get_all_tweets(stub)
        return all_tweets


def get_tweets(username):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = twitter_clone_pb2_grpc.TweetServiceStub(channel)
        all_tweets = helpers.get_tweets(stub, username)
        return all_tweets


def create_tweet(username, content, tags):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = twitter_clone_pb2_grpc.TweetServiceStub(channel)
        tweet_new = helpers.create_tweet(stub, username, content, tags)
        print(tweet_new)
        return tweet_new


def remove_tweet(tweet_id):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = twitter_clone_pb2_grpc.TweetServiceStub(channel)
        helpers.remove_tweet(stub, tweet_id)


def edit_tweet(tweet_id, new_content, new_tags):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = twitter_clone_pb2_grpc.TweetServiceStub(channel)
        helpers.edit_tweet(stub, tweet_id, new_content, new_tags)
