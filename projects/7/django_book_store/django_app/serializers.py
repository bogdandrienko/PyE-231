from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django_app import models


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        # fields = ["username", "email"]
        # fields = "__all__"
        exclude = ["password", "last_login"]

    def get_groups(self, obj: User):
        """Вычисляемое поле, в сериализатор для модели User, которое
        выводит списком через запятую все группы к которым принадлежит
        пользователь"""
        try:
            _groups: [Group] = obj.groups.order_by("name")
            _names = ""
            for i in _groups:
                _names += f"{i.name}, "
            return f"{_names[:-2]}"
        except Exception as error:
            return ""


class BookSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"
