"""
django_settings/urls.py - Маршрутизация на уровне проекта
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("django_app.urls")),  # вложение
    path("", include("django_profiles.urls")),  # вложение
    path("vacansie/", include("django_vacansie.urls")),
    # приложения
    # path("", include('payment.urls')),
    # path("", include('blog.urls')),
    # path("", include('chat.urls')),
]
