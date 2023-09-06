from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from timecatcherapi.models import FollowUser, User
from rest_framework import filters

class FollowUserView(ViewSet):
    """Timeline view"""
    
    def list(self, request):
        """Handle GET requests to get all events
        Returns:
            Response -- JSON serialized list of events
        """
        followuser = FollowUser.objects.all()
        serializer = FollowUserSerializer(followuser, many=True)
        return Response(serializer.data)  
    
    def retrieve(self, request, pk):
        try:
            followuser = FollowUser.objects.get(pk=pk)
            serializer = FollowUserSerializer(followuser)
            return Response(serializer.data)
        except FollowUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
          
    def create(self, request):
        user_id1 = User.objects.get(pk=request.data["followingUser"])
        user_id2 = User.objects.get(pk=request.data["followedUser"])# Assuming user_id is provided in the request data
        followuser = FollowUser.objects.create(
            followingUser=user_id1,
            followedUser=user_id2,
        )
        serializer = FollowUserSerializer(followuser)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
    def destroy(self, request, pk):
        followuser = FollowUser.objects.get(pk=pk)
        followuser.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)      

class FollowUserSerializer(serializers.ModelSerializer):
    """JSON serializer for timelines"""
    class Meta:
        model = FollowUser
        fields = ('id', 'followingUser','followedUser')
        depth =1