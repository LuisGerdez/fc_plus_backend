from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GameLevel(models.TextChoices):
        BEGINNER = "B", "Beginner"
        INTERMEDIATE = "I", "Intermediate"
        ADVANCED = "A", "Advanced"
        PROFESSIONAL = "P", "Professional"

    class Gender(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
        OTHER = "O", "Other"

    class Position(models.TextChoices):
        GOALKEEPER = "GK", "Goalkeeper"
        DEFENDER = "DF", "Defender"
        MIDFIELDER = "MF", "Midfielder"
        FORWARD = "FW", "Forward"

    birthdate = models.DateField(null=True, blank=True)
    game_level = models.CharField(max_length=20, choices=GameLevel.choices, default=GameLevel.BEGINNER)
    gender = models.CharField(max_length=10, choices=Gender.choices, null=True, blank=True)
    languages = models.JSONField(default=list, blank=True)  # Example: ["en", "es"]
    nationality = models.CharField(max_length=100, null=True, blank=True)
    preferred_position = models.CharField(max_length=20, choices=Position.choices, null=True, blank=True)
    promo_code = models.CharField(max_length=50, null=True, blank=True)