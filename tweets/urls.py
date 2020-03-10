from django.urls import path
from .views import Home, MyTweets, UserTweets, CreateTweet, RemoveTweet, EditTweet

urlpatterns = [
    path('home', Home.as_view(), name='home'),
    path('my_tweets', MyTweets.as_view(), name='my_tweets'),
    path('user_tweets/<str:user>', UserTweets.as_view(), name='user_tweets'),
    path('create_tweet', CreateTweet.as_view(), name='create_tweet'),
    path('remove_tweet', RemoveTweet.as_view(), name='remove_tweet'),
    path('edit_tweet', EditTweet.as_view(), name='edit_tweet'),
]
