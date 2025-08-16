from django.contrib import admin
from django.urls import path, include
from djoser.social.views import ProviderAuthView
from core.views import GoogleLoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    
    path('o/<str:provider>/', ProviderAuthView.as_view(), name='provider-auth'),
    path("auth/google_login/", GoogleLoginView.as_view(), name="google-oauth-login"),

    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path('auth/', include('djoser.social.urls')),
]