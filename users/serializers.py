from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import serializers


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField(required=False)
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user is not None and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentials")
