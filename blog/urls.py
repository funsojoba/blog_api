from django.urls import path
from .views import PostList, PostDetails, UserList, UserDetail


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetails.as_view()),
    path('users/', UserList.as_view(), name='user'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user_detail')
    ]