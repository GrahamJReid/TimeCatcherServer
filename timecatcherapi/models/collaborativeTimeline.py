from django.db import models
from .users import User

class CollaborativeTimeline(models.Model):
    """Model that represents a post"""
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')
    title = models.CharField(max_length=50)
    image_url = models.CharField(max_length=1000)
    public = models.BooleanField()
    gallery = models.BooleanField()
    date_added = models.IntegerField()
