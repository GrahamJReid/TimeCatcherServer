from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from timecatcherapi.models import Thread, User, Event
from rest_framework import filters

class ThreadView(ViewSet):
    """Timeline view"""
    filter_backends = [filters.SearchFilter]
    search_fields = ['title',]
    
    
    def list(self, request):
        """Handle GET requests to get all timelines
        Returns:
            Response -- JSON serialized list of timelines
        """
        thread = Thread.objects.all()
        serializer = ThreadSerializer(thread, many=True)
        return Response(serializer.data)
      
    def retrieve(self, request, pk):
        try:
            thread = Thread.objects.get(pk=pk)
            serializer = ThreadSerializer(thread)
            return Response(serializer.data)
        except Thread.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
          
    def create(self, request):
        user_id = User.objects.get(pk=request.data["user"])
        event_id = Event.objects.get(pk=request.data["event"])# Assuming user_id is provided in the request data
        thread = Thread.objects.create(
            user=user_id,
            event=event_id,
            title=request.data["title"],
            date=request.data["date"],
            description=request.data["description"]
        )
        serializer = ThreadSerializer(thread)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def update(self, request, pk):
        user_id = User.objects.get(pk=request.data["user"])
        event_id = Event.objects.get(pk=request.data["event"])
        
        thread = Thread.objects.get(pk=pk)
        thread.title = request.data["title"]
        thread.date = request.data["date"]
        thread.description = request.data["description"]
        thread.user=user_id
        thread.event=event_id
        
        thread.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        thread = Thread.objects.get(pk=pk)
        thread.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)      

class ThreadSerializer(serializers.ModelSerializer):
    """JSON serializer for timelines"""
    class Meta:
        model = Thread
        fields = ('id', 'user', 'title', 'event', 'date','description')
        depth =1
