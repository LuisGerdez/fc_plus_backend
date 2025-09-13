from django.db import models
from django.conf import settings
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
    public_profile = models.BooleanField(default=True)


class SoccerField(models.Model):
    name = models.CharField(max_length=150)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=255)
    google_maps_link = models.URLField(max_length=500, blank=True, null=True)
    capacity = models.PositiveIntegerField(default=0)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Match(models.Model):
    class MatchType(models.TextChoices):
        FIVE_VS_FIVE = "5v5", "5 vs 5"
        SEVEN_VS_SEVEN = "7v7", "7 vs 7"
        EIGHT_VS_EIGHT = "8v8", "8 vs 8"

    class Status(models.TextChoices):
        AVAILABLE = "available", "Available"
        IN_PROGRESS = "in_progress", "In progress"
        FINISHED = "finished", "Finished"

    datetime = models.DateTimeField(verbose_name="Match date & time")
    field = models.ForeignKey("SoccerField", on_delete=models.CASCADE, related_name="matches")
    match_type = models.CharField(max_length=10, choices=MatchType.choices, default=MatchType.FIVE_VS_FIVE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="hosted_matches")
    players = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="joined_matches", blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.AVAILABLE)

    class Meta:
        ordering = ["-datetime"]
        verbose_name = "Match"
        verbose_name_plural = "Matches"

    def get_max_players(self):
        if self.match_type == self.MatchType.FIVE_VS_FIVE:
            return 10
        elif self.match_type == self.MatchType.SEVEN_VS_SEVEN:
            return 14
        elif self.match_type == self.MatchType.EIGHT_VS_EIGHT:
            return 16
            
        return 0

    def __str__(self):
        return f"{self.MatchType(self.match_type).label} - {self.field.name} @ {self.datetime:%Y-%m-%d %H:%M}"