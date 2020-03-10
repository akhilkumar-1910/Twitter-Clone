from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Tweet, Tag

# Create your views here.
def home(request):
    print(request.user)
    all_tweets = Tweet.objects.all().order_by('-last_edited')
    users = User.objects.all()
    return render(request, 'home.html', context={'all_tweets': all_tweets, 'users': users})

def my_tweets(request):
    username = request.user.username
    my_tweets = Tweet.objects.filter(user__username=username).order_by('-last_edited')
    users = User.objects.all()
    return render(request, 'my_tweets.html', context={'my_tweets': my_tweets, 'users': users})

def user_tweets(request, user):
    user_tweets = Tweet.objects.filter(user__username=user).order_by('-last_edited')
    users = User.objects.all()
    return render(request, 'user_tweets.html', context={'user_tweets': user_tweets, 'users': users})


def create_tweet(request):
    if request.method == "POST":
        message = request.POST.get("message")
        tags = request.POST.get("tag")
        tags = tags.split()
        username=request.user.username
        user = User.objects.filter(username = username)
        #print(user[0])
        tweet = Tweet(message=message, user=user[0])
        tweet.save()
        for tag in tags:
            t = Tag(tag_name=tag, tweet=tweet)
            t.save()
        return redirect('my_tweets')
    else:
        return redirect('my_tweets')

def remove_tweet(request):
    if request.method == "POST":
        tweet_id = request.POST.get("tweet_id")
        Tweet.objects.filter(id=tweet_id).delete()
        return redirect('my_tweets')
    else:
        return redirect('my_tweets')