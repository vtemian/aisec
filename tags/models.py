from discussion.models import Post
from django.contrib import admin

__author__ = 'Vlad Temian'

from django.db import models
from django.contrib.auth.models import User

class TagPriority(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)

    value = models.IntegerField(max_length=3, default=0)
    color = models.CharField(max_length=25, default="#FFFFF")

class Tag(models.Model):
    name = models.CharField(max_length=150)
    user = models.ManyToManyField(User, null=True, through="tags.TagsUser")

    post = models.ForeignKey(Post)
    priority = models.ForeignKey(TagPriority)

class TagsUser(models.Model):
    user = models.ForeignKey(User)
    tag = models.ForeignKey(Tag)

class AdminTagPriority(admin.ModelAdmin):
    pass
admin.site.register(TagPriority, AdminTagPriority)
admin.site.register(Tag)