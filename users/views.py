from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import RegisterSerializer, UserSerializer, LoginSerializer


# Register user API
class RegisterUser(APIView):
    def post(self, request):
        register_serializer = RegisterSerializer(data=request.data)
        if not register_serializer.is_valid():
            return Response(register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user = register_serializer.save()
        return Response({
            "user": UserSerializer(user).data,
            "token": Token.objects.create(user=user).key
        })


# Login user API
class LoginUser(APIView):
    def post(self, request):
        login_serializer = LoginSerializer(data=request.data)
        if not login_serializer.is_valid():
            return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user = login_serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user).data,
            "token": token.key
        })
