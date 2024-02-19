from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.api),
    path("native/", views.api_native),
    path("users/", views.api_users),
]
