from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.api.serializers import RegistrationSerializer, PostSerializer
from accounts.models import Account, Post


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
