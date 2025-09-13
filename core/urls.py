from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("users/", views.UserViewSet.as_view({"get": "list", "post": "create"}), name="users"),
    path("users/<int:pk>/", views.UserViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="users"),
    
    path("users/me", views.UserViewSet.as_view({"get": "me_update", "put": "me_update", "patch": "me_update"}), name="users_me"),

    path("soccer-fields/", views.SoccerFieldViewSet.as_view({"get": "list", "post": "create"}), name="soccerfields_list"),
    path("soccer-fields/<int:pk>/", views.SoccerFieldViewSet.as_view({ "get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="soccerfields_detail"),
]