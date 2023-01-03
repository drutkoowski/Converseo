from rest_framework import serializers
from accounts.models import UserProfile, Account


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=105, min_length=6)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=100)
    gender = serializers.CharField(max_length=6, write_only=True)
    birth_date = serializers.DateField(write_only=True)

    class Meta:
        model = Account
        fields = ("username", "email", "password","gender", "birth_date")

    def validate(self, args):
        email = args.get('email', None)
        username = args.get("username", None)

        if Account.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'email already exists'})
        if Account.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": 'username already exists'})

        return super().validate(args)

    def create(self, validated_data):
        gender = validated_data.pop('gender', None)
        birth_date = validated_data.pop('birth_date', None)
        account = Account.objects.create_user(**validated_data)
        user_profile = UserProfile.objects.create(user=account, gender=gender, date_of_birth=birth_date)
        return account