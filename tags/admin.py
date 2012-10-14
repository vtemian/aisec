from django.contrib import admin
from tags.models import TagPriority, Tag, TagsPost, TagsUser

__author__ = 'wok'

class AdminTagPriority(admin.ModelAdmin):
    list_display = ('name', 'description', 'value')

class AdminTag(admin.ModelAdmin):
    list_display = ['name']

class AdminTagUser(admin.ModelAdmin):
  list_display = ('user', 'tag')

class AdminTagsPost(admin.ModelAdmin):
    list_display = ('post', 'tag')

admin.site.register(TagPriority, AdminTagPriority)
admin.site.register(Tag, AdminTag)
admin.site.register(TagsUser, AdminTagUser)
admin.site.register(TagsPost, AdminTagsPost)