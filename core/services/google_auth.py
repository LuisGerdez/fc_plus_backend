import jwt, urllib, requests
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from social_django.models import UserSocialAuth

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
        email = decoded["email"]

        user = cls.get_or_create_user(email)
        tokens = cls.get_jwt_tokens(user)
        return {"access": tokens["access"], "refresh": tokens["refresh"]}

    @staticmethod
    def get_or_create_user(email):
        user, created = User.objects.get_or_create(email=email, defaults={"username": email})
        if created:
            UserSocialAuth.create_social_auth(user=user, provider="google-oauth2-custom", uid=email)
        return user

    @staticmethod
    def get_jwt_tokens(user):
        refresh = RefreshToken.for_user(user)
        return {"access": str(refresh.access_token), "refresh": str(refresh)}