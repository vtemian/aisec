from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
import json
import urllib
import medals

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    gravatar_url = models.CharField(max_length=100)
    facebook_id = models.BigIntegerField(null=True)
    access_token = models.CharField(max_length=150)

    def get_facebook_profile(self):
        fb_profile = urllib.urlopen('https://graph.facebook.com/me?access_token=%s' % self.access_token)
        return json.load(fb_profile)

class UserStats(models.Model):
    user = models.ForeignKey(UserProfile)

    money = models.IntegerField(null=True, default=10)
    exp = models.IntegerField(null=True, default=0)
    lvl = models.IntegerField(default=1)
    rank = models.CharField(max_length=30, default='Second Lieutenant')
    achieve_points = models.IntegerField(default=0)

    won = models.IntegerField(null=True, default=0)
    lost = models.IntegerField(null=True, default=0)
    medals=models.ManyToManyField(medals.models.Medal, through='UserMedals', null=True)

class Weapon(models.Model):
    name = models.CharField(max_length=200, default='a')
    image = models.CharField(max_length=50, default='ImagePath')

    description = models.TextField(null=True)

class UserDivision(models.Model):
    user = models.ForeignKey(UserStats)
    name = models.CharField(max_length=30, default='D')

    points = models.IntegerField(max_length=30, default=0)

    matches_played = models.IntegerField(max_length=30, default=0)
    weapons = models.ManyToManyField(Weapon, through='UserWeapons', null=True)


class UserWeapons(models.Model):
    user = models.ForeignKey(UserDivision)
    weapon= models.ForeignKey(Weapon)

    qty = models.IntegerField(default=0, max_length=50)

    on = models.BooleanField(default=False)

class PasswordReset(models.Model):
    email = models.EmailField(max_length=50)
    token = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=datetime.now)
    done = models.BooleanField(default=False)

class UserMedals(models.Model):
    user = models.ForeignKey(UserStats)
    medals= models.ForeignKey(medals.models.Medal)