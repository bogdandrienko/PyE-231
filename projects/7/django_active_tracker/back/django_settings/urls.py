from django.urls import path, include

urlpatterns = [
    path("", include("django_app.urls")),
]
