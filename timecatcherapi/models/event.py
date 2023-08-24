from django.db import models
from .users import User

class Event(models.Model):
    """Model that represents a post"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id_id')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    image_url = models.CharField(max_length=1000)
    date = models.DateField()
    color= models.CharField(max_length=50)
    BCE = models.BooleanField(default=False)
