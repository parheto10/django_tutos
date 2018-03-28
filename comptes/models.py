# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete='CASCADE')
    description = models.CharField(max_length=120, default='')
    ville = models.CharField(max_length=120)
    site_web = models.URLField(blank=True)
    contacts = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __unicode__(self):
        return self.user.username

def nv_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(nv_profile, sender=User)


# Create your models here.
