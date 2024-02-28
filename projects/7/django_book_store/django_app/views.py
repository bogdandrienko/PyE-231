import time

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from django_app import models, serializers

"""
Есть данные, которые нельзя видеть/менять/удалять... всем подряд.

* Новости на главной странице(список). - они общедоступны. [auth(аутентификация) - нет, role(авторизация) - нет]
* Публикация новости. - только зарегистированным пользователям. [auth - да, role(авторизация) - нет]
* Редактирование профиля. - и админ и сам пользователь. [auth - да, role(авторизация) - да]
* Список всех пользователей системы(с личными данными). - они строго по определённому уровню доступа. [auth - да, role - да]

Аутентификация - "залогиниться", т.е. войти под своим аккаунтом.
Авторизация - "определить уровень доступа", т.е. понять может ли этот пользователь делать это действие.

sessionid - Токен аутентификации.

Active - если отключить, в систему нельзя аутентифицироваться.
Staff status - позволяет входить в админ часть сайта.
Superuser status - даёт все права.

sessionid - Django MVT (не подходит для api)

Django DRF - REST-api
API - программный интерфейс(общение двух программ). JSON -> JSON

- если чужая система не умеет сохранять в кукесы session_id,
этой системе придёт в КАЖДОМ запросе присылать логин и пароль.

В каждом запросе посылать логин и пароль нельзя.

* JWT(Json Web Token)-token:
* Фронтендер присылает Вам логин и пароль.
* Создать токен и послать в чужую систему. И следующие 10(N) минут, запросы которые идут с этим токеном,
* мы считаем, что они от этого пользователя.

{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NzgxMTkxMywiaWF0IjoxNjk3NzI1NTEzLCJqdGkiOiI3N2VkMGJjYmJjM2E0Yzc0OGE2MTM4NDczMzE0NTA2NCIsInVzZXJfaWQiOjJ9.giR_jtqJBSFJJ2j5klHrqtvgUygQbLFSiR7IeTmITN4",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3NzI1ODEzLCJpYXQiOjE2OTc3MjU1MTMsImp0aSI6IjcyOWM4ZmE1MWFkMzRmNDlhOGYwYzc1MzZlNzkwZTJlIiwidXNlcl9pZCI6Mn0.RGEGt9XJKyxWfY0qkG4gk9yY0QMbood4BDFTL9-PwxY"
}

{
    "refresh": - одноразовый токен для обновления токенов
    "access": - токен доступа, его будет фронтендер присылать каждый раз внутри headers
}
"""


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "build/index.html", {})


@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])  # 1 ур - всем
def api(request: Request) -> Response:
    print(request.user)
    return Response(data={"message": "OK"})


@api_view(http_method_names=["GET"])
@permission_classes([IsAdminUser])  # 2 ур - всем, кто аутентифицирован
def api_users(request: Request) -> Response:
    print(request.user)
    return Response(data={"message": User.objects.all()[0].password})


@api_view(http_method_names=["POST"])
@permission_classes([AllowAny])
def api_user_register(request: Request) -> Response:
    print("request.data: ", request.data)

    username = request.data.get("username", None)
    password = request.data.get("password", None)
    if username and password:
        # TODO НЕЛЬЗЯ ВЕРИТЬ FRONTEND! - нужна регулярка для валидации
        User.objects.create(username=username, password=make_password(password))
        # User.objects.create_user(username=username, password=password)
        return Response(data={"success": "Account succesfully created!"}, status=status.HTTP_200_OK)
    else:
        return Response(data={"error": "Login or password is incorrect"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def api_book(request: Request) -> Response:
    try:
        time.sleep(1)
        if request.method == "GET":
            _obj = models.Book.objects.all()
            _json = serializers.BookSimpleSerializer(_obj, many=True if isinstance(_obj, QuerySet) else False).data
            return Response(data={"success": _json})
    except Exception as error:
        return Response(data={"error": str(error)}, status=400)


@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])
def api_book_id(request: Request, book_id: str) -> Response:
    try:
        time.sleep(1)
        if request.method == "GET":
            _obj = models.Book.objects.get(id=int(book_id))
            _json = serializers.BookSimpleSerializer(_obj, many=True if isinstance(_obj, QuerySet) else False).data
            return Response(data={"success": _json})
    except Exception as error:
        return Response(data={"error": str(error)}, status=400)
