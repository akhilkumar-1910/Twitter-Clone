from proto import twitter_clone_pb2_grpc
from .helpers import Helper
# import grpc


class TweetServicer(twitter_clone_pb2_grpc.TweetServiceServicer):
    def GetAllTweets(self, request, context):
        helper = Helper()
        all_tweets = helper.get_all_tweets()
        for tweet in all_tweets:
            yield tweet

    def GetTweets(self, request, context):
        helper = Helper()
        all_tweets = helper.get_tweets(request)
        for tweet in all_tweets:
            yield tweet

    def CreateTweet(self, request, context):
        helper = Helper()
        response = helper.create_tweet(request)
        return response

    def RemoveTweet(self, request, context):
        helper = Helper()
        helper.remove_tweet(request)

    def EditTweet(self, request, context):
        helper = Helper()
        response = helper.edit_tweet(request)
        return response
