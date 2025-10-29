from django.contrib import admin

from .models import LostItem, FoundItem, UserProfile

# Register your models here
admin.site.register(LostItem)
admin.site.register(FoundItem)
admin.site.register(UserProfile)
