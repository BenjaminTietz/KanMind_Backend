from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "full_name",
            "email",
            "password",
            "repeated_password",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def validate(self, attrs):
        password = attrs.get("password")
        repeated_password = attrs.get("repeated_password")

        if password != repeated_password:
            raise serializers.ValidationError(
                {"repeated_password": "Passwords do not match."}
            )

        return attrs

    def create(self, validated_data):
        validated_data.pop("repeated_password")

        user = User.objects.create_user(
            username=validated_data["email"],
            email=validated_data["email"],
            full_name=validated_data["full_name"],
            password=validated_data["password"],
        )
        return user
