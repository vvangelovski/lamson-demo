from django.contrib.admin import ModelAdmin, StackedInline, site
from models import Topic, Post, Subscription

class PostInlineAdmin(StackedInline):
    model = Post

class TopicAdmin(ModelAdmin):
    inlines = [PostInlineAdmin,]

class SubscriptionAdmin(ModelAdmin):
    pass



site.register(Topic, TopicAdmin)
site.register(Subscription, SubscriptionAdmin)

