from django.contrib import admin

from .models import Topic, Card


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass

