from django.db import models
from timecatcherapi.models import User,Event,Thread

class ThreadComment(models.Model):
    """Model that represents a post"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000000)
    date = models.IntegerField()