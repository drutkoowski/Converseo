from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.api.permissions import IsEditedUser
from accounts.api.serializers import RegistrationSerializer, AccountSerializer
from accounts.models import Account


class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = RegistrationSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return serializer.data


class UserUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsEditedUser]
    authentication_classes = []
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return serializer.data


class GetCurrentUserAPIView(APIView):

    def get(self, request):
        user = Account.objects.filter(pk=request.user.pk).first()
        if user is not None:
            serializer = AccountSerializer(user, context={"request": request})
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
