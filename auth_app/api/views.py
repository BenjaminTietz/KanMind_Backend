from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from .serializers import RegistrationSerializer, LoginSerializer

User = get_user_model()


class RegisterAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)

        response_data = {
            "token": token.key,
            "fullname": user.full_name,
            "email": user.email,
            "user_id": user.id,
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)

        response_data = {
            "token": token.key,
            "fullname": user.full_name,
            "email": user.email,
            "user_id": user.id,
        }

        return Response(response_data, status=status.HTTP_200_OK)
