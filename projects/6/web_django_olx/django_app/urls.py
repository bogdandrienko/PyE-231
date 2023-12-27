from django.urls import path
from django_app import views

urlpatterns = [
    #    URL      view    name
    path("", views.home, name="home"),
    path("items_list/", views.item_list, name="items_list"),
    path("register/", views.register, name="register"),  # {% url 'register' %}
    path("login/", views.login_v, name="login"),
    path("logout/", views.logout_v, name="logout"),
]
