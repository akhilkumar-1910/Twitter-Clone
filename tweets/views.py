from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.models import User
from grpc_service.client.client import (
    get_all_tweets,
    get_tweets,
    create_tweet,
    remove_tweet,
    edit_tweet,
)


class Home(ListView):

    context_object_name = "all_tweets"
    template_name = "home.html"

    def get_queryset(self):
        # return Tweet.objects.all().order_by("-last_edited")
        return get_all_tweets()

    def get_context_data(self):
        context = super().get_context_data()
        context["users"] = User.objects.all()
        # print(context)
        return context


class MyTweets(ListView):

    context_object_name = "my_tweets"
    template_name = "my_tweets.html"

    def get_queryset(self):
        # return Tweet.objects.filter(user__username=self.request.user).order_by('-last_edited')
        return get_tweets(self.request.user.username)

    def get_context_data(self):
        context = super().get_context_data()
        context["users"] = User.objects.all()
        # print(context)
        return context


class UserTweets(ListView):

    context_object_name = "user_tweets"
    template_name = "user_tweets.html"

    def get_queryset(self):
        return get_tweets(self.kwargs["user"])

    def get_context_data(self):
        context = super().get_context_data()
        context["users"] = User.objects.all()
        # print(context)
        return context


class CreateTweet(ListView):
    def post(self, request):
        content = request.POST.get("message")
        tags = request.POST.get("tag")
        tags = tags.strip()
        tags = tags.split()
        username = request.user.username
        tweet = create_tweet(username, content, tags)
        print(tweet)
        return redirect("my_tweets")

    def get(self, request):
        return redirect("my_tweets")


class RemoveTweet(ListView):
    def post(self, request):
        tweet_id = request.POST.get("tweet_id")
        remove_tweet(int(tweet_id))
        return redirect("my_tweets")

    def get(self, request):
        return redirect("my_tweets")


class EditTweet(ListView):
    def post(self, request):
        tweet_id = request.POST.get("tweet_id")
        new_content = request.POST.get("edited_tweet")
        print(new_content)
        new_tags = request.POST.get("edited_tag")
        new_tags = new_tags.strip()
        new_tags = new_tags.split()
        edit_tweet(int(tweet_id), new_content, new_tags)
        return redirect("my_tweets")

    def get(self, request):
        return redirect("my_tweets")
