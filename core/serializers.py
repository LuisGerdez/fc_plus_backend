from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import SoccerField, Match

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


class MatchSerializer(serializers.ModelSerializer):
    host = serializers.StringRelatedField(read_only=True)
    field = SoccerFieldSerializer(read_only=True)
    players = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    players_count = serializers.SerializerMethodField()
    max_players_amount = serializers.SerializerMethodField()

    class Meta:
        model = Match
        fields = [
            "id",
            "datetime",
            "field",
            "match_type",
            "price",
            "host",
            "players",
            "players_count",
            "max_players_amount",
            "status",
        ]
        read_only_fields = ["id", "status"]

    def get_players_count(self, obj):
        return obj.players.count()

    def get_max_players_amount(self, obj):
        return obj.get_max_players()


class MatchDetailSerializer(serializers.ModelSerializer):
    host = UserSerializer(read_only=True)
    field = SoccerFieldSerializer(read_only=True)
    field_id = serializers.PrimaryKeyRelatedField(source="field", queryset=SoccerField.objects.all(), write_only=True)
    players = UserSerializer(many=True, read_only=True)
    players_count = serializers.SerializerMethodField()
    max_players_amount = serializers.SerializerMethodField()

    class Meta:
        model = Match
        fields = [
            "id",
            "datetime",
            "field",
            "field_id",
            "match_type",
            "price",
            "host",
            "players",
            "players_count",
            "max_players_amount",
            "status",
        ]
    
    def get_players_count(self, obj):
        return obj.players.count()

    def get_max_players_amount(self, obj):
        return obj.get_max_players()