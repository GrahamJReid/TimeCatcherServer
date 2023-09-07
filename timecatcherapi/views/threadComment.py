from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from timecatcherapi.models import ThreadComment, User,Thread
from rest_framework import filters

class ThreadCommentView(ViewSet):
    """Event view"""
    def list(self, request):
        """Handle GET requests to get all events
        Returns:
            Response -- JSON serialized list of events
        """
        threadcomment = ThreadComment.objects.all()
        serializer = ThreadCommentSerializer(threadcomment, many=True)
        return Response(serializer.data)
      
    def retrieve(self, request, pk):
        try:
            threadcomment = ThreadComment.objects.get(pk=pk)
            serializer = ThreadCommentSerializer(threadcomment)
            return Response(serializer.data)
        except ThreadComment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
          
    def create(self, request):
        user_id = User.objects.get(pk=request.data["user"])
        thread_id = Thread.objects.get(pk=request.data["thread"])
       
        threadcomment = ThreadComment.objects.create(
            user=user_id,
            thread=thread_id,
            content=request.data["content"],
            date=request.data["date"]    
        )
        serializer = ThreadCommentSerializer(threadcomment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def update(self, request, pk):
        user_id = User.objects.get(pk=request.data["user"])
        thread_id = Thread.objects.get(pk=request.data["thread"])
        threadcomment = ThreadComment.objects.get(pk=pk)
        threadcomment.content = request.data["content"]
        threadcomment.date = request.data["date"]
        threadcomment.user = user_id
        threadcomment.thread=thread_id
        
        threadcomment.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        threadcomment = ThreadComment.objects.get(pk=pk)
        threadcomment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)      

class ThreadCommentSerializer(serializers.ModelSerializer):
    """JSON serializer for events"""
    class Meta:
        model = ThreadComment
        fields = ('id', 'user', 'thread', 'content', 'date')
        depth = 1