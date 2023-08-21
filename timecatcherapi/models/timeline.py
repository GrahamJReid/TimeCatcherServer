from django.db import models
from .users import User

class Timeline(models.Model):
    """Model that represents a post"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,db_column='user_id_id')
    title = models.CharField(max_length=50)
    image_url = models.CharField(max_length=1000)
    public = models.BooleanField()
    gallery = models.BooleanField()
    date_added = models.IntegerField()
