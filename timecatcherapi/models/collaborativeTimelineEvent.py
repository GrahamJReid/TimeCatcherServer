from django.db import models
from timecatcherapi.models import Event, CollaborativeTimeline

class CollaborativeTimelineEvent(models.Model):
    """Model that represents a post"""
    timeline_id = models.ForeignKey(CollaborativeTimeline, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    