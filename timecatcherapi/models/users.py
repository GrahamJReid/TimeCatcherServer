from django.db import models

class User(models.Model):
    """Model that represents a rare user"""
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    image_url = models.CharField(max_length=1000)  # Change to ImageField and specify the upload directory
    uid = models.CharField(max_length=10000)
