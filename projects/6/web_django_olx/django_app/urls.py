from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.home, name="home"),
    #
    path("search/", views.search, name="search"),
    path("category/", views.category, name="category"),
    path("category/<str:slug_name>/", views.items, name="items"),
    path("item/<str:item_id>/", views.item, name="item"),
    path("comment/", views.comment, name="comment"),
    #
    path("register/", views.register, name="register"),  # {% url 'register' %}
    path("login/", views.login_v, name="login"),
    path("logout/", views.logout_v, name="logout"),
]
