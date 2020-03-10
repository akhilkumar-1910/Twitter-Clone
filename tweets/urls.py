from django.views.generic import TemplateView
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('my_tweets', views.my_tweets, name='my_tweets'),
    path('create_tweet', views.create_tweet, name='create_tweet'),
]