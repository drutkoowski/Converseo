from django.urls import path
from . import views

urlpatterns = [
    path("user/create",  views.UserCreateAPIView.as_view(), name="user-create"),
    path("user/current",  views.GetCurrentUserAPIView.as_view(), name="user-get"),
    path("queue/create",  views.CreateQueueAPIView.as_view(), name="queue-create"),
    path('queue/delete', views.DeleteQueueAPIView.as_view(), name='delete-queue'),
    path('queue/get-talker', views.RandomizeQueuedAPIView.as_view(), name='get-talker'),
    path("posts", views.PostListCreateAPIView.as_view(), name='list-create-post')
]