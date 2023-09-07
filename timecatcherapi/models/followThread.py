from django.db import models
from timecatcherapi.models import User, Thread

class FollowThread(models.Model):
    """Model that represents a post"""
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)