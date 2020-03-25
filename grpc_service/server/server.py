from proto import twitter_clone_pb2_grpc
from .helpers import get_all_tweets, get_tweets, create_tweet, remove_tweet, edit_tweet


class TweetServicer(twitter_clone_pb2_grpc.TweetServiceServicer):
    def GetAllTweets(self, request, context):
        all_tweets = get_all_tweets()
        for tweet in all_tweets:
            yield tweet

    def GetTweets(self, request, context):
        all_tweets = get_tweets(request)
        for tweet in all_tweets:
            yield tweet

    def CreateTweet(self, request, context):
        create_tweet(request)
        return request

    def RemoveTweet(self, request, context):
        remove_tweet(request)
        return request

    def EditTweet(self, request, context):
        edit_tweet(request)
        return request
