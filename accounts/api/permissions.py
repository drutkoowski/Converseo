from jwt import decode as jwt_decode
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions
from django.conf import settings

User = get_user_model()


def get_user(validated_token):
    try:
        user = get_user_model().objects.get(id=validated_token["user_id"])
        return user
    except User.DoesNotExist:
        return AnonymousUser()


class IsEditedUser(permissions.BasePermission):

    def has_permission(self, request, view):
        bearer = request.headers["Authorization"]
        token = bearer.replace('Bearer', '').strip()
        decoded_data = jwt_decode(
            token, settings.SECRET_KEY, algorithms=["HS256"]
        )
        user = get_user(decoded_data)
        if user is not AnonymousUser:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        bearer = request.headers["Authorization"]
        token = bearer.replace('Bearer', '').strip()
        decoded_data = jwt_decode(
            token, settings.SECRET_KEY, algorithms=["HS256"]
        )
        user = get_user(decoded_data)
        if user is not AnonymousUser and obj == user:
            return True
        return False
