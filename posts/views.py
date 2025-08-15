from django.shortcuts import get_object_or_404, render
from .models import Post
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import PostSerializer

class PostViewSet(viewsets.ViewSet):

    def list(self, request:Request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request:Request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
