from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tweet(models.Model):
    message = models.CharField(max_length=300)
    posted = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

class Tag(models.Model):
    tag_name = models.CharField(max_length=100, null=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag_name



