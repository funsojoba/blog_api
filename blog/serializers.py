from .models import Post
from rest_framework import serializers
from django.contrib.auth import get_user_model


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'title', 'body', 'created_at')


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')