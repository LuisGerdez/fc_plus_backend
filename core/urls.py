from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("users/", views.UserViewSet.as_view({"get": "list"}), name="users"),
    path("users/<int:pk>/", views.UserViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="users"),
    path("users/me", views.UserViewSet.as_view({"put": "me_update", "patch": "me_update"}), name="users_me"),
]