from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from timecatcherapi.models import CollaborativeTimelineEvent, Event, CollaborativeTimeline

class CollaborativeTimelineEventView(ViewSet):
    """TimelineEvent view"""
    
    def list(self, request):
        """Handle GET requests to get all timeline events
        Returns:
            Response -- JSON serialized list of timeline events
        """
        timeline_events = CollaborativeTimelineEvent.objects.all()
        serializer = CollaborativeTimelineEventSerializer(timeline_events, many=True)
        return Response(serializer.data)
      
    def retrieve(self, request, pk):
        try:
            timeline_event = CollaborativeTimelineEvent.objects.get(pk=pk)
            serializer = CollaborativeTimelineEventSerializer(timeline_event)
            return Response(serializer.data)
        except CollaborativeTimelineEvent.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
          
    def create(self, request):
        timeline_id = CollaborativeTimeline.objects.get(pk=request.data["timelineId"])
        event_id = Event.objects.get(pk=request.data["eventId"])
        timeline_event = CollaborativeTimelineEvent.objects.create(
            timeline_id=timeline_id,
            event_id=event_id
        )
        serializer = CollaborativeTimelineEventSerializer(timeline_event)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def destroy(self, request, pk):
        timeline_event = CollaborativeTimelineEvent.objects.get(pk=pk)
        timeline_event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)      

class CollaborativeTimelineEventSerializer(serializers.ModelSerializer):
    """JSON serializer for timeline events"""
    class Meta:
        model = CollaborativeTimelineEvent
        fields = ('id', 'timeline_id', 'event_id')
        depth = 1
