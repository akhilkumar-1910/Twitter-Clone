from django.views.generic import TemplateView
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('my_tweets', views.my_tweets, name='my_tweets'),
    path('user_tweets/<str:user>', views.user_tweets, name='user_tweets'),
    path('create_tweet', views.create_tweet, name='create_tweet'),
    path('remove_tweet', views.remove_tweet, name='remove_tweet'),
    path('edit_tweet', views.edit_tweet, name='edit_tweet'),
]