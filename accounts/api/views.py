from rest_framework import generics
from accounts.api.serializers import RegistrationSerializer
from accounts.models import Account


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
