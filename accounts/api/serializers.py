from rest_framework import serializers
from accounts.models import Account


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
        return account