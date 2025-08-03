from rest_framework import serializers
from .

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = 