"""
django_app/urls.py - Маршрутизация на приложения
"""
from django.urls import path
from django_app import views

urlpatterns = [
    # домашняя страница
    #    url    view(def)   name
    path("", views.home, name=""),
    path("home", views.home, name="home"),
    path("index", views.home, name="index"),
    # форма для заполнения
    path("blank", views.blank, name="blank"),
    # test
    path("test", views.test, name="test"),
    # todo new (ORM + Cache + Pagination)
    # path("vacansie/list/", views.vacansie_list, name="vacansie_list"),
    # path("vacansie/detail/<str:vac_id>/", views.home, name="test"),
    # path("vacansie/create/", views.home, name="test"),
    # path("vacansie/export/", views.home, name="test"),
    # path("vacansie/import/", views.home, name="test"),
    # path("", views.home),
    # path("", views.home),
    # path("", views.home),
    # path("", views.home),
]
