from django.urls import path
from . import views

urlpatterns = [
    path("user/create",  views.UserCreateAPIView.as_view(), name="user-create"),
    path("queue/create",  views.CreateQueueAPIView.as_view(), name="queue-create"),
    path('queue/delete', views.DeleteQueueAPIView.as_view(), name='delete-queue'),
    path("posts", views.PostListCreateAPIView.as_view(), name='list-create-post')
]