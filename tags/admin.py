from django.contrib import admin
from tags.models import TagPriority, Tag, TagsPost

__author__ = 'wok'

class AdminTagPriority(admin.ModelAdmin):
    list_display = ('name', 'description', 'value')

class AdminTag(admin.ModelAdmin):
    list_display = ['name']

class AdminTagsPost(admin.ModelAdmin):
    list_display = ('post', 'tag')


admin.site.register(TagPriority, AdminTagPriority)
admin.site.register(Tag, AdminTag)
admin.site.register(TagsPost, AdminTagsPost)