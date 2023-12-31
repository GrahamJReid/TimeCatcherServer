from django.db import models
from timecatcherapi.models import User,Event

class Thread(models.Model):
    """Model that represents a post"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    description = models.CharField(max_length=100000, default='No Description')
    title = models.CharField(max_length=1000)
    date = models.IntegerField()
