"""
django_app/urls.py - Маршрутизация на приложения
"""
from django.urls import path
from django_vacansie import views

urlpatterns = [
    path("list/", views.vacansie_list, name="vacansie_list"),
    path("detail/<str:vac_id>/", views.vacansie_detail, name="vacansie_detail"),
    path("create/", views.vacansie_create, name="vacansie_create"),
    # path("change/", views.vacansie_create, name="vacansie_create"),
    # path("delete/", views.vacansie_create, name="vacansie_create"),
    # path("export/", views.home, name="test"),
    # path("import/", views.home, name="test"),
]
