"""
django_profiles/urls.py - Маршрутизация на приложения
"""
from django.urls import path
from django_profiles import views

urlpatterns = [
    # форма для заполнения и отправки
    path("resume_form/", views.resume_form, name="resume_form"),
    # приём формы и сохранение пользователя
    path("save_form/", views.save_form, name="save_form"),
    # список профилей
    path("profiles/", views.profiles, name="profiles"),
    # профиль
    path("profile/<str:pk>/", views.profile, name="profile"),
    # удаление профиля
    path("profile/delete/<str:pk>/", views.profile_delete, name="profile_delete"),
]
