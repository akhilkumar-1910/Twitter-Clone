from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.models import User
from .models import Tweet, Tag


class Home(ListView):

    context_object_name = 'all_tweets'
    template_name = 'home.html'

    def get_queryset(self):
        return Tweet.objects.all().order_by("-last_edited")

    def get_context_data(self):
        context = super().get_context_data()
        context['users'] = User.objects.all()
        # print(context)
        return context


class MyTweets(ListView):

    context_object_name = 'my_tweets'
    template_name = 'my_tweets.html'

    def get_queryset(self):
        return Tweet.objects.filter(user__username=self.request.user).order_by('-last_edited')

    def get_context_data(self):
        context = super().get_context_data()
        context['users'] = User.objects.all()
        # print(context)
        return context


class UserTweets(ListView):

    context_object_name = 'user_tweets'
    template_name = 'user_tweets.html'

    def get_queryset(self):
        queryset = Tweet.objects.filter(user__username=self.kwargs['user']).order_by('-last_edited')
        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        context['users'] = User.objects.all()
        print(context)
        return context


class CreateTweet(ListView):

    def post(self, request):
        message = request.POST.get("message")
        tags = request.POST.get("tag")
        tags = tags.split()
        username = request.user.username
        user = User.objects.filter(username=username)
        tweet = Tweet(message=message, user=user[0])
        tweet.save()
        for tag in tags:
            t = Tag(tag_name=tag, tweet=tweet)
            t.save()
        print("here")
        return redirect('my_tweets')

    def get(self, request):
        return redirect('my_tweets')


class RemoveTweet(ListView):

    def post(self, request):
        tweet_id = request.POST.get("tweet_id")
        Tweet.objects.filter(id=tweet_id).delete()
        return redirect('my_tweets')

    def get(self, request):
        return redirect('my_tweets')


class EditTweet(ListView):

    def post(self, request):
        tweet_id = request.POST.get("tweet_id")
        tweet = Tweet.objects.get(id=tweet_id)
        new_message = request.POST.get("edited_tweet")
        tweet.message = new_message
        tweet.save()
        return redirect('my_tweets')

    def get(self, request):
        return redirect('my_tweets')
