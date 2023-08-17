from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from timecatcherapi.models import Timeline, User

class TimelineView(ViewSet):
    """Timeline view"""
    
    def list(self, request):
        """Handle GET requests to get all timelines
        Returns:
            Response -- JSON serialized list of timelines
        """
        timelines = Timeline.objects.all()
        serializer = TimelineSerializer(timelines, many=True)
        return Response(serializer.data)
      
    def retrieve(self, request, pk):
        try:
            timeline = Timeline.objects.get(pk=pk)
            serializer = TimelineSerializer(timeline)
            return Response(serializer.data)
        except Timeline.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
          
    def create(self, request):
        user_id = User.objects.get(pk=request.data["userId"])  # Assuming user_id is provided in the request data
        timeline = Timeline.objects.create(
            user_id=user_id,
            title=request.data["title"],
            image_url=request.data["imageUrl"],
            public=request.data["public"],
            gallery=request.data["gallery"],
            date_added=request.data["dateAdded"]
        )
        serializer = TimelineSerializer(timeline)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def update(self, request, pk):
        user_id = User.objects.get(pk=request.data["userId"])
        timeline = Timeline.objects.get(pk=pk)
        timeline.title = request.data["title"]
        timeline.image_url = request.data["imageUrl"]
        timeline.public = request.data["public"]
        timeline.gallery = request.data["gallery"]
        timeline.date_added = request.data["dateAdded"]
        timeline.user_id=user_id
        
        timeline.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        timeline = Timeline.objects.get(pk=pk)
        timeline.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)      

class TimelineSerializer(serializers.ModelSerializer):
    """JSON serializer for timelines"""
    class Meta:
        model = Timeline
        fields = ('id', 'user_id', 'title', 'image_url', 'public', 'gallery', 'date_added')
        depth =1