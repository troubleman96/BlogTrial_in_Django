from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    tittle = serializers.

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created']