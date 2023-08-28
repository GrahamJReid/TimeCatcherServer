from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from timecatcherapi.models import Event, User
from rest_framework import filters

class EventView(ViewSet):
    """Event view"""
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'date','BCE']
    def list(self, request):
        """Handle GET requests to get all events
        Returns:
            Response -- JSON serialized list of events
        """
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
      
    def retrieve(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        except Event.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
          
    def create(self, request):
        user_id = User.objects.get(pk=request.data["userId"])  # Assuming user_id is provided in the request data
        event = Event.objects.create(
            user_id=user_id,
            title=request.data["title"],
            description=request.data["description"],
            image_url=request.data["imageUrl"],
            date=request.data["date"],
            color=request.data["color"],
            BCE=request.data["BCE"]
        )
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def update(self, request, pk):
        user_id = User.objects.get(pk=request.data["userId"])
        event = Event.objects.get(pk=pk)
        event.title = request.data["title"]
        event.description = request.data["description"]
        event.image_url = request.data["imageUrl"]
        event.date = request.data["date"]
        event.color = request.data["color"]
        event.BCE = request.data["BCE"]
        event.user_id = user_id
        
        event.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)      

class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events"""
    class Meta:
        model = Event
        fields = ('id', 'user_id', 'title', 'description', 'image_url', 'date', 'color','BCE')
        depth = 1
