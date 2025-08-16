import jwt, urllib, requests
from rest_framework_simplejwt.tokens import RefreshToken
from social_django.models import UserSocialAuth
from django.contrib.auth import get_user_model

User = get_user_model()

class GoogleAuthService:
    CLIENT_ID = '58380115097-i539jmejqghecfpl0iacci13fgmhl2lb.apps.googleusercontent.com'
    CLIENT_SECRET = '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'
    REDIRECT_URI = "http://localhost:3000/auth/complete/google/"
    TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"

    @classmethod
    def exchange_code_for_tokens(cls, code):
        payload = {
            "code": code,
            "client_id": cls.CLIENT_ID,
            "client_secret": cls.CLIENT_SECRET,
            "redirect_uri": cls.REDIRECT_URI,
            "grant_type": "authorization_code",
        }

        response = requests.post(cls.TOKEN_ENDPOINT, data=urllib.parse.urlencode(payload),
                                 headers={"content-type": "application/x-www-form-urlencoded"})
        if not response.ok:
            print("Failed to exchange code:", response.text)
            raise Exception("Failed to exchange code")

        id_token = response.json()["id_token"]
        decoded = jwt.decode(id_token, options={"verify_signature": False})

        email = decoded.get("email", "")
        first_name = decoded.get("given_name", "")
        last_name = decoded.get("family_name", "")

        if not "email":
            raise Exception("Email not found in ID token")

        user = cls.get_or_create_user(email, first_name, last_name)
        tokens = cls.get_jwt_tokens(user)
        return {"access": tokens["access"], "refresh": tokens["refresh"]}

    @staticmethod
    def get_or_create_user(email, first_name="", last_name=""):
        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                "username": email,
                "first_name": first_name,
                "last_name": last_name,
            }
        )

        if created:
            UserSocialAuth.create_social_auth(user=user, provider="google-oauth2-custom", uid=email)
        return user

    @staticmethod
    def get_jwt_tokens(user):
        refresh = RefreshToken.for_user(user)
        return {"access": str(refresh.access_token), "refresh": str(refresh)}