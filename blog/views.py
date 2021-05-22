from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializers
from .permissions import IsAuthorOrReadOnly



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers

# Create your views here.
