from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from timecatcherapi.models import TimelineEvent, Event, Timeline

class TimelineEventView(ViewSet):
    """TimelineEvent view"""
    
    def list(self, request):
        """Handle GET requests to get all timeline events
        Returns:
            Response -- JSON serialized list of timeline events
        """
        timeline_events = TimelineEvent.objects.all()
        serializer = TimelineEventSerializer(timeline_events, many=True)
        return Response(serializer.data)
      
    def retrieve(self, request, pk):
        try:
            timeline_event = TimelineEvent.objects.get(pk=pk)
            serializer = TimelineEventSerializer(timeline_event)
            return Response(serializer.data)
        except TimelineEvent.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
          
    def create(self, request):
        timeline_id = Timeline.objects.get(pk=request.data["timelineId"])
        event_id = Event.objects.get(pk=request.data["eventId"])
        timeline_event = TimelineEvent.objects.create(
            timeline_id=timeline_id,
            event_id=event_id
        )
        serializer = TimelineEventSerializer(timeline_event)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def destroy(self, request, pk):
        timeline_event = TimelineEvent.objects.get(pk=pk)
        timeline_event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)      

class TimelineEventSerializer(serializers.ModelSerializer):
    """JSON serializer for timeline events"""
    class Meta:
        model = TimelineEvent
        fields = ('id', 'timeline_id', 'event_id')
        depth = 1
