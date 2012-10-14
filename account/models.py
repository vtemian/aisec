from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
import json
import urllib
from tags.models import Tag

class UserProfile(models.Model):
  user = models.OneToOneField(User)

  position = models.CharField(max_length=30, null=True)
  phone = models.CharField(max_length=30, null=True)
  adress = models.CharField(max_length=30, null=True)
  how_long_time_in_aeisec = models.CharField(max_length=30, null=True)
  university = models.CharField(max_length=30, null=True)