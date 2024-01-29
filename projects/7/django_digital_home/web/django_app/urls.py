from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.index),
    path("settings/get/", views.settings_get),
    path("settings/set/", views.settings_set),
    path("settings/change/", views.settings_change, name="settings_change"),
    # path("settings/set/", views.settings_get),
    # path("events/current/", include("django_app.urls")),
    # path("events/history/", include("django_app.urls")),
]
