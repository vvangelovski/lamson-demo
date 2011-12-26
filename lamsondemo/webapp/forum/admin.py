from django.contrib.admin import ModelAdmin, site
from models import Topic, Post, Subscription

class TopicAdmin(ModelAdmin):
    pass

class SubscriptionAdmin(ModelAdmin):
    pass



site.register(Topic, TopicAdmin)
site.register(Subscription, SubscriptionAdmin)

