from __future__ import unicode_literals
from django.db import models

class Twitter_user(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=255)
    screen_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True)
    friends_count = models.IntegerField()
    followers_count = models.IntegerField()
    email = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    time_zone = models.CharField(max_length=255, null=True)
    user_since = models.DateTimeField(auto_now_add=False, null=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=7, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=7, null=True)
    profile_img = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "ScreenName: {}\nName: {}\n".format(self.screen_name, self.name)
