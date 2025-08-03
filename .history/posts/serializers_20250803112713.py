from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = post