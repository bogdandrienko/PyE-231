"""
django_settings/models.py - модели(таблицы, сущности) в базе данных
"""
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator, MaxLengthValidator
from django.db import models
from django.utils import timezone


# миграция(migrations) - применение изменений на базе данных
