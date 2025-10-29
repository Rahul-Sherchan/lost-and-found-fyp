from django.db import models
from django.contrib.auth.models import User

class LostItem(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    description = models.TextField()
    location_lost = models.CharField(max_length=200)
    date_lost = models.DateTimeField()
    image = models.ImageField(upload_to='lost_items/')
    date_posted = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name

class FoundItem(models.Model):
    finder = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    description = models.TextField()
    location_found = models.CharField(max_length=200)
    date_found = models.DateTimeField()
    image = models.ImageField(upload_to='found_items/')
    date_posted = models.DateTimeField(auto_now_add=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
