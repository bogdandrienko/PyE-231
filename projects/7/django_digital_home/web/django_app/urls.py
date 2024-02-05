from django.urls import path
from django_app import views

urlpatterns = [
    # base
    path("", views.home, name="home"),
    path("api/", views.api),
    # params GET/POST
    path("api/params/", views.params),
    # messages GET/POST
    path("api/messages/", views.messages),
    # old
    path("api/settings/change/", views.settings_change, name="settings_change"),
]
