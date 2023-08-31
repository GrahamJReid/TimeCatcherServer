from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from timecatcherapi.models import Timeline, Event, TimelineEvent, User

# Define the serializers directly in the view file
class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events"""
    class Meta:
        model = Event
        fields = ('id', 'user_id', 'title', 'description', 'image_url', 'date', 'color', 'BCE','isPrivate')
        

class TimelineEventSerializer(serializers.ModelSerializer):
    """JSON serializer for timeline events"""
    class Meta:
        model = TimelineEvent
        fields = ('id', 'timeline_id', 'event_id')
       

class TimelineSerializer(serializers.ModelSerializer):
    """JSON serializer for timelines"""
    class Meta:
        model = Timeline
        fields = ('id', 'user_id', 'title', 'image_url', 'public', 'gallery', 'date_added')
        

@api_view(['POST'])
def create_timeline_and_events(request):
    try:
        data = request.data
        user_id = request.data['userId']
        user = User.objects.get(pk=request.data["userId"]) 
        print(user_id, "this is what the userId comes back as for comparing", user)
        # Retrieve the User instance

        timeline_data = data['timeline']
        event_data = data['events']

        # Create a new timeline with the retrieved User instance
        timeline_data['user_id'] = user.id
        print(timeline_data, 'timeline data appened?')
        timeline_serializer = TimelineSerializer(data=timeline_data)

        if timeline_serializer.is_valid():
            timeline = timeline_serializer.save()

            # Create events and link them to the timeline
            created_events = []
            for event in event_data:
                event['user_id'] = user.id  # Assign the User instance
                event_serializer = EventSerializer(data=event)
                if event_serializer.is_valid():
                    created_event = event_serializer.save()
                    TimelineEvent.objects.create(timeline_id=timeline, event_id=created_event)
                    created_events.append(created_event)
                else:
                    return JsonResponse({'error': event_serializer.errors}, status=400)

            return JsonResponse({'message': 'Timeline and events created successfully'})
        else:
            return JsonResponse({'error': timeline_serializer.errors}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
