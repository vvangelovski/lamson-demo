from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    title = models.CharField(max_length = 255)

    def __unicode__(self):
        return self.title

class Post(models.Model):
    topic = models.ForeignKey(Topic)
    content = models.TextField()

    def __unicode__(self):
        return self.topic.title

class Subscription(models.Model):
    subscriber = models.ForeignKey(User)
    topic = models.ForeignKey(Topic)

    def __unicode__(self):
        return "%s - %s"%(self.subscirber.username, topic.title)

class ReplyAddress(models.Model):
    subscription = models.ForeignKey(Subscription)
    address = models.EmailField()

    def __unicode__(self):
        return self.address
