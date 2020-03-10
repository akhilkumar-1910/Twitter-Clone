from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Tweet, Tag

# Create your views here.
def home(request):
    all_tweets = Tweet.objects.all()
    print(request.POST)
    return render(request, 'home.html', context={'all_tweets': all_tweets})

def my_tweets(request):
    if request.method == "POST":
        username = request.POST.get("username")
        user_tweets = Tweet.objects.filter(user__username=username)
        return render(request, 'my_tweets.html', context={'user_tweets': user_tweets})
    else:
        return redirect('home')

def create_tweet(request):
    if request.method == "POST":
        message = request.POST.get("message")
        tags = request.POST.get("tag")
        tags = tags.split()
        username=request.POST.get("username")
        user = User.objects.filter(username = username)
        #print(user[0])
        tweet = Tweet(message=message, user=user[0])
        tweet.save()
        for tag in tags:
            t = Tag(tag_name=tag, tweet=tweet)
            t.save()
        return redirect('home')
    else:
        return redirect('home')