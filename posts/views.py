from django.shortcuts import get_object_or_404, render
from .models import Post
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status, generics, mixins
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import PostSerializer
from .permissions import ReadOnly, AuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):

    permission_classes = [AuthorOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ListPostsView(generics.GenericAPIView,
                    mixins.ListModelMixin):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        return Post.objects.filter(author=user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)