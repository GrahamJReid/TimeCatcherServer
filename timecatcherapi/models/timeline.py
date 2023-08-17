from django.db import models
from .users import User

class Timeline(models.Model):
    """Model that represents a post"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image_url = models.CharField(max_length=50)
    public = models.BooleanField()
    gallery = models.BooleanField()
    date_added = models.IntegerField()