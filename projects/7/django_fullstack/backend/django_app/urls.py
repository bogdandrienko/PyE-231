from django.urls import path
from django_app import views

urlpatterns = [
    path("api/users", views.api_users),
    path("api/user/credit/check/", views.api_user_credit_check),
]
