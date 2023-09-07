from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from timecatcherapi.models import FollowThread, User,Thread
from rest_framework import filters

class FollowThreadView(ViewSet):
    """Timeline view"""
    
    def list(self, request):
        """Handle GET requests to get all events
        Returns:
            Response -- JSON serialized list of events
        """
        followthread = FollowThread.objects.all()
        serializer = FollowThreadSerializer(followthread, many=True)
        return Response(serializer.data)  
    
    def retrieve(self, request, pk):
        try:
            followthread = FollowThread.objects.get(pk=pk)
            serializer = FollowThreadSerializer(followthread)
            return Response(serializer.data)
        except FollowThread.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
          
    def create(self, request):
        user_id = User.objects.get(pk=request.data["user"])
        thread_id = Thread.objects.get(pk=request.data["thread"])# Assuming user_id is provided in the request data
        followthread = FollowThread.objects.create(
            thread=thread_id,
            user=user_id,
        )
        serializer = FollowThreadSerializer(followthread)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
    def destroy(self, request, pk):
        followuser = FollowThread.objects.get(pk=pk)
        followuser.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)      

class FollowThreadSerializer(serializers.ModelSerializer):
    """JSON serializer for timelines"""
    class Meta:
        model = FollowThread
        fields = ('id', 'thread','user')
        depth =1