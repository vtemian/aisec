from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
import json
import urllib

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    gravatar_url = models.CharField(max_length=100)
    facebook_id = models.BigIntegerField(null=True)
    access_token = models.CharField(max_length=150)