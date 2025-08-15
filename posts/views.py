from django.shortcuts import get_object_or_404, render
from .models import Post
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer