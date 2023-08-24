from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, serializers

from timecatcherapi.models import Event, TimelineEvent

@api_view(['GET'])
def events_by_timeline(request, pk):
    class EventSerializer(serializers.ModelSerializer):
        """JSON serializer for events"""
        class Meta:
            model = Event
            fields = ('id', 'user_id', 'title', 'description', 'image_url', 'date', 'color','BCE')
            depth = 1
    
    try:
        timeline_events = TimelineEvent.objects.filter(timeline_id=pk)
        events = [timeline_event.event_id for timeline_event in timeline_events]
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    except TimelineEvent.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)



