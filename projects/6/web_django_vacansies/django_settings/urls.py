"""
django_settings/urls.py - Маршрутизация на уровне проекта
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('django_app.urls')),  # вложение
    # приложения
    # path("", include('payment.urls')),
    # path("", include('blog.urls')),
    # path("", include('chat.urls')),
]
