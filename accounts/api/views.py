from django.http import Http404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.api.serializers import RegistrationSerializer, PostSerializer, CreateQueueSerializer
from accounts.models import Account, Post, SearchQueue


class UserCreateAPIView(generics.CreateAPIView):
    """Provide the answers queryset of a specific question instance."""
    # serializer_class = AnswerSerializer
    # permission_classes = [IsAuthenticated]
    serializer_class = RegistrationSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        # serializer.save(user=self.request.user)


class PostListCreateAPIView(generics.ListCreateAPIView):
    """Provide the answers queryset of a specific question instance."""
    # serializer_class = AnswerSerializer
    # permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        # serializer.save(user=self.request.user)


class CreateQueueAPIView(generics.CreateAPIView):
    """Provide the answers queryset of a specific question instance."""
    serializer_class = CreateQueueSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return serializer.data


class DeleteQueueAPIView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def delete(self, request, format=None):
        queues = SearchQueue.objects.filter(user=request.user).all()
        for queue in queues:
            queue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
