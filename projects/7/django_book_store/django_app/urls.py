from django.urls import path
from django_app import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("", views.index),
    path("home/", views.index),
    path("index/", views.index),
    path("api/", views.api),
    # JWT(json web token) authentication
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    #
    path("api/users/", views.api_users),
    path("api/user/register/", views.api_user_register),
    #
    # GET(many), POST
    path("api/book/", views.api_book),
    # GET(one), PUT, DELETE
    path("api/book/<str:book_id>/", views.api_book_id),
]
