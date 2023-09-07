from django.db import models
from timecatcherapi.models import Event, Timeline

class TimelineEvent(models.Model):
    """Model that represents a timelineEvent"""
    timeline_id = models.ForeignKey(Timeline, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    