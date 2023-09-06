from django.db import models
from .users import User

class FollowUser(models.Model):
    """Model that represents a post"""
    followingUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followingUser')
    followedUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followedUser')
 