import re

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django_app import models


# @login_required
def home(request):
    # custom(самописное)
    # if not request.user.is_authenticated:
    #     return redirect(reverse("login"))
    return render(request, "HomePage.html")


def item_list(request):
    items = models.Item.objects.all().filter(is_active=True).order_by("-price", "-title")
    return render(request, "ItemListPage.html", context={"items": items})


def register(request):
    if request.method == "GET":
        return render(request, "RegisterPage.html")
    elif request.method == "POST":
        # print(request.POST, type(request.POST))
        username = str(request.POST["username"])
        password = str(request.POST["password"])

        if not re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$', password):
            # todo - не успешная регистрация -> вывод ошибки (Regex pattern) - complex password
            # raise Exception("Invalid password")
            return render(request, "RegisterPage.html", context={"error": "Пароль не соответствует сложности!"})

        # ORM vs raw SQL
        # создание нового пользователя
        usr = User.objects.create(username=username, password=make_password(password))
        """
INSERT INTO User 
    (username, password) 
VALUES 
    (:username, :password)
        """
        # вход в аккаунт
        login(request, usr)  # create cookie -> session id
        # logout(request)  # delete cookie -> session id

        # todo - успешная регистрация -> автологин и отправка на страницу с объявления
        return redirect(reverse("items_list"))


def login_v(request):
    if request.method == "GET":
        return render(request, "LoginPage.html")
    elif request.method == "POST":
        username = str(request.POST["username"])  # из формы
        password = str(request.POST["password"])  # из формы

        # аутентификация - проверяет наличие пользователя с таким логин+пароль
        # авторизация - проверят права
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, "LoginPage.html", context={"error": "Логин или пароль не совпадают!"})
        login(request, user)
        return redirect(reverse("items_list"))


def logout_v(request):
    logout(request)
    return redirect(reverse("login"))
