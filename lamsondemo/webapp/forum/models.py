from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    title = models.CharField(max_length = 255)

class Post(models.Model):
    topic = models.ForeignKey(Post)
    content = models.TextField()

class Subscription(models.Model):
    subscriber = models.ForeignKey(User)
    topic = models.ForeignKey(Topic)

