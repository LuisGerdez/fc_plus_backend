from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import SoccerField

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
            "public_profile",
            "is_superuser",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id", "username", "email", "first_name", "last_name", "is_superuser",
            "birthdate", "game_level", "gender", "languages",
            "nationality", "preferred_position", "promo_code", "public_profile"
        ]


class SoccerFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoccerField
        fields = [
            "id",
            "name",
            "image_url",
            "address",
            "google_maps_link",
            "capacity",
            "is_enabled",
        ]
        read_only_fields = ["id", "created_at"]