from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "birthdate",
            "game_level",
            "gender",
            "languages",
            "nationality",
            "preferred_position",
            "promo_code",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id", "username", "email", "first_name", "last_name",
            "birthdate", "game_level", "gender", "languages",
            "nationality", "preferred_position", "promo_code"
        ]