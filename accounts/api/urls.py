from django.urls import path
from . import views

urlpatterns = [
    path("user/create",  views.UserCreateAPIView.as_view(), name="user-create"),
    path("user/edit/<int:pk>",  views.UserUpdateAPIView.as_view(), name="user-edit"),
    path("user/current",  views.GetCurrentUserAPIView.as_view(), name="user-get"),
]
