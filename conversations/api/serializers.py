from rest_framework import serializers
from accounts.api.serializers import AccountSerializer
from accounts.models import Account
from conversations.models import SearchQueue, Conversation


class QueueSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = SearchQueue
        fields = ["user", "created_at", "expires_at"]

    def get_user(self, instance):
        request = self.context.get("request")
        user = Account.objects.get(pk=request.user.pk)
        return user.username

    def create(self, validated_data):
        request = self.context.get("request")
        search_queue = SearchQueue(user__pk=request.user.pk)
        search_queue.save()


class ConversationSerializer(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True, many=True)

    class Meta:
        model = Conversation
        fields = "__all__"

