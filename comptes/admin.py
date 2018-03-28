# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserProfile

admin.site.site_header = 'Admin'

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_info', 'ville', 'contacts', 'site_web']

    def user_info(self, obj):
        return obj.description

    user_info.short_description = 'Infos'


admin.site.register(UserProfile, UserProfileAdmin)




# Register your models here.
