from .models import Post
from rest_framework import serializers


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'title', 'body', 'created_at')