from rest_framework import serializers
from accounts.models import Account, Post, SearchQueue


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=105, min_length=6)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=100)

    class Meta:
        model = Account
        fields = ("username", "email", "password")

    def validate(self, args):
        email = args.get('email', None)
        username = args.get("username", None)

        if Account.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'email already exists'})
        if Account.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": 'username already exists'})

        return super().validate(args)

    def create(self, validated_data):
        account = Account.objects.create_user(**validated_data)
        account.is_active = True
        account.save()
        return account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("email", "id", "username", "avatar")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("author",)

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        return post


class CreateQueueSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = SearchQueue
        fields = ("user",
                  "created_at", "expires_at")

    def get_user(self, instance):
        request = self.context.get("request")
        user = Account.objects.get(pk=request.user.pk)
        return user.username

    def create(self, validated_data):
        request = self.context.get("request")
        user = Account.objects.get(pk=request.user.pk)
        search_queue = SearchQueue.objects.create(user=user)
        return search_queue
