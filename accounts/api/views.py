from django.db.models import Q
from django.db.models.functions import Now
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.api.serializers import RegistrationSerializer, PostSerializer, CreateQueueSerializer, AccountSerializer
from accounts.models import Post, SearchQueue, Account


class UserCreateAPIView(generics.CreateAPIView):
    """Provide the answers queryset of a specific question instance."""
    # serializer_class = AnswerSerializer
    permission_classes = []
    authentication_classes = []
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
    Retrieve, update or delete a queue instance.
    """

    def delete(self, request, format=None):
        queues = SearchQueue.objects.filter(user=request.user).all()
        for queue in queues:
            queue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RandomizeQueuedAPIView(APIView):
    """
    Retrieve, update or delete a queue instance.
    """

    def get(self, request):
        queue = SearchQueue.objects.exclude(Q(user=request.user) | Q(expires_at__lte=Now())).first()
        if queue is not None:
            serializer = AccountSerializer(queue.user)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class GetCurrentUserAPIView(APIView):

    def get(self, request):
        user = Account.objects.filter(pk=request.user.pk).first()
        if user is not None:
            serializer = AccountSerializer(user)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

### SIMPLE JWT

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         refresh = self.get_token(self.user)
#         data['refresh'] = str(refresh)
#         data['access'] = str(refresh.access_token)
#
#         # Add extra responses here
#         data['username'] = self.user.username
#         return data
#
#
# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer
