
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

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
        # serializer.save(user=self.request.user)


# class CreateQueueAPIView(generics.CreateAPIView):
#     """Provide the answers queryset of a specific question instance."""
#     serializer_class = CreateQueueSerializer
#
#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         context.update({"request": self.request})
#         return context
#
#     def perform_create(self, serializer):
#         if serializer.is_valid():
#             serializer.save()
#             return serializer.data


# class DeleteQueueAPIView(APIView):
#     """
#     Retrieve, update or delete a queue instance.
#     """
#
#     def delete(self, request, format=None):
#         queues = SearchQueue.objects.filter(user=request.user).all()
#         for queue in queues:
#             queue.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class RandomizeQueuedAPIView(APIView):
#     """
#     Retrieve, update or delete a queue instance.
#     """
#
#     def get(self, request):
#         queue = SearchQueue.objects.exclude(Q(user=request.user) | Q(expires_at__lte=Now())).first()
#         if queue is not None:
#             serializer = AccountSerializer(queue.user, context={"request": request})
#             SearchQueue.objects.filter(Q(user=request.user) | Q(expires_at__lte=Now())).first().delete()
#             queue.delete()
#             return Response(status=status.HTTP_200_OK, data={'e': '2', 'user': serializer.data})
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)


class GetCurrentUserAPIView(APIView):

    def get(self, request):
        user = Account.objects.filter(pk=request.user.pk).first()
        if user is not None:
            serializer = AccountSerializer(user, context={"request": request})
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)



