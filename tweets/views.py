from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response

from grpc_service.client.client import Client


class Home(APIView):
    """ Home consists of all the tweets """

    def get(self, request):
        grpc_client = Client()
        all_tweets = grpc_client.get_all_tweets()
        return Response(all_tweets)


# class Home(ListView):

#     context_object_name = "all_tweets"
#     template_name = "home.html"
#     client = Client()

#     def get_queryset(self):
#         # return Tweet.objects.all().order_by("-last_edited")
#         print(type(self.client.get_all_tweets()))
#         return self.client.get_all_tweets()

#     def get_context_data(self):
#         context = super().get_context_data()
#         context["users"] = User.objects.all()
#         # print(context)
#         return context


class MyTweets(APIView):
    """ Tweets of particular user """

    def get(self, request):
        try:
            username = request.query_params["username"]
        except KeyError:
            return Response(status=404)
        grpc_client = Client()
        my_tweets = grpc_client.get_tweets(username)
        if len(my_tweets) == 0:
            return Response(status=404)
        return Response(my_tweets)


# class MyTweets(ListView):

#     context_object_name = "my_tweets"
#     template_name = "my_tweets.html"
#     client = Client()

#     def get_queryset(self):
#         # return Tweet.objects.filter(user__username=self.request.user).order_by('-last_edited')
#         return self.client.get_tweets(self.request.user.username)

#     def get_context_data(self):
#         context = super().get_context_data()
#         context["users"] = User.objects.all()
#         # print(context)
#         return context


class UserTweets(APIView):
    """ Tweets for a user """

    def get(self, request, *args, **kwargs):
        grpc_client = Client()
        user_tweets = grpc_client.get_tweets(kwargs["user"])
        return Response(user_tweets)


# class UserTweets(ListView):

#     context_object_name = "user_tweets"
#     template_name = "user_tweets.html"
#     client = Client()

#     def get_queryset(self):
#         return self.client.get_tweets(self.kwargs["user"])

#     def get_context_data(self):
#         context = super().get_context_data()
#         context["users"] = User.objects.all()
#         # print(context)
#         return context


class CreateTweet(APIView):

    client = Client()

    def post(self, request):
        content = request.POST.get("message")
        tags = request.POST.get("tag")
        tags = tags.strip()
        tags = tags.split()
        username = request.user.username
        tweet = self.client.create_tweet(username, content, tags)
        return Response(tweet)


class RemoveTweet(APIView):

    client = Client()

    def post(self, request):
        tweet_id = request.POST.get("tweet_id")
        self.client.remove_tweet(int(tweet_id))
        return Response(status=204)


class EditTweet(APIView):

    client = Client()

    def post(self, request):
        tweet_id = request.POST.get("tweet_id")
        new_content = request.POST.get("edited_tweet")
        print(new_content)
        new_tags = request.POST.get("edited_tag")
        new_tags = new_tags.strip()
        new_tags = new_tags.split()
        self.client.edit_tweet(int(tweet_id), new_content, new_tags)
        return Response(status=204)
