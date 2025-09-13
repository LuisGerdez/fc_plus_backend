from django.http import HttpResponse
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.decorators import action

from .serializers import UserSerializer, SoccerFieldSerializer, MatchSerializer, MatchDetailSerializer
from .models import SoccerField, Match
from .services.google_auth import GoogleAuthService

User = get_user_model()


def index(request):
    return HttpResponse("Hello world!")


class GoogleLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        code = request.data.get('code')
        if not code:
            return Response({'error': 'No code provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            result = GoogleAuthService.exchange_code_for_tokens(code)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["put", "patch", "get"])
    def me_update(self, request):
        if request.method == "GET":
            serializer = self.get_serializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        partial = request.method == "PATCH"

        serializer = self.get_serializer(request.user, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_permissions(self):
        """
        Return permissions based on action:
        - 'me_update': Authenticated users
        - All other actions: Admin users
        """
        if self.action == "me_update":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


class SoccerFieldViewSet(viewsets.ModelViewSet):
    queryset = SoccerField.objects.all()
    serializer_class = SoccerFieldSerializer

    def get_permissions(self):
        """
        Return permissions based on method:
        GET/HEAD/OPTIONS = Authenticated users
        POST/PUT/PATCH/DELETE = Admin users
        """
        if self.request.method in ("GET", "HEAD", "OPTIONS"):
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return MatchSerializer

        return MatchDetailSerializer