from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from timecatcherapi.models import CollaborativeTimeline, User
from rest_framework import filters

class CollaborativeTimelineView(ViewSet):
    """Timeline view"""
    filter_backends = [filters.SearchFilter]
    search_fields = ['title',]
    
    
    def list(self, request):
        """Handle GET requests to get all timelines
        Returns:
            Response -- JSON serialized list of timelines
        """
        timelines = CollaborativeTimeline.objects.all()
        serializer = TimelineSerializer(timelines, many=True)
        return Response(serializer.data)
      
    def retrieve(self, request, pk):
        try:
            timeline = CollaborativeTimeline.objects.get(pk=pk)
            serializer = TimelineSerializer(timeline)
            return Response(serializer.data)
        except CollaborativeTimeline.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
          
    def create(self, request):
        user_id1 = User.objects.get(pk=request.data["user1"])
        user_id2 = User.objects.get(pk=request.data["user2"])# Assuming user_id is provided in the request data
        timeline = CollaborativeTimeline.objects.create(
            user1=user_id1,
            user2=user_id2,
            title=request.data["title"],
            image_url=request.data["imageUrl"],
            public=request.data["public"],
            gallery=request.data["gallery"],
            date_added=request.data["dateAdded"]
        )
        serializer = TimelineSerializer(timeline)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def update(self, request, pk):
        user1 = User.objects.get(pk=request.data["user1"])
        user2 = User.objects.get(pk=request.data["user2"])
        timeline = CollaborativeTimeline.objects.get(pk=pk)
        timeline.title = request.data["title"]
        timeline.image_url = request.data["imageUrl"]
        timeline.public = request.data["public"]
        timeline.gallery = request.data["gallery"]
        timeline.date_added = request.data["dateAdded"]
        timeline.user1=user1
        timeline.user2=user2
        
        timeline.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        timeline = CollaborativeTimeline.objects.get(pk=pk)
        timeline.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)      

class TimelineSerializer(serializers.ModelSerializer):
    """JSON serializer for timelines"""
    class Meta:
        model = CollaborativeTimeline
        fields = ('id', 'user1','user2', 'title', 'image_url', 'public', 'gallery', 'date_added')
        depth =1
