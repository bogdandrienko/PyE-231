from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.home),
    path("prices/", views.prices, name="prices"),
    path("animals/", views.animals, name="animals"),
    path("generate/", views.generate),
]
