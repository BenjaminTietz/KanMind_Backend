from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status


class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        return Response(
            {"detail": "Registration endpoint placeholder"},
            status=status.HTTP_501_NOT_IMPLEMENTED,
        )


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        return Response(
            {"detail": "Login endpoint placeholder"},
            status=status.HTTP_501_NOT_IMPLEMENTED,
        )
