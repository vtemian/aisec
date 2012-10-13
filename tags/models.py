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

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=150)
    user = models.ManyToManyField(User, null=True, through="tags.TagsUser")
    post = models.ManyToManyField(Post, null=True, through="tags.TagsPost")

    priority = models.ForeignKey(TagPriority)

    def __unicode__(self):
        return self.name

class TagsUser(models.Model):
    user = models.ForeignKey(User)
    tag = models.ForeignKey(Tag)

class TagsPost(models.Model):
    post = models.ForeignKey(Post)
    tag = models.ForeignKey(Tag)

    def __unicode__(self):
        return 'Tag {tag} for {post}'.format(
            tag=self.tag.name,
            post=self.post.pk
        )