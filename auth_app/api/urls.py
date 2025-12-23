from django.urls import path

from .views import LoginAPIView, RegisterAPIView

urlpatterns = [
    path("registration/", RegisterAPIView.as_view(), name="registration"),
    path("login/", LoginAPIView.as_view(), name="login"),
]
