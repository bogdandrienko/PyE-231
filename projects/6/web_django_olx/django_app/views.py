import datetime
import re

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django_app import models


def home(request):
    categories = models.CategoryItem.objects.all()
    vips = models.Vip.objects.all().filter(expired__gt=datetime.datetime.now()).order_by("priority", "-article")
    return render(request, "HomePage.html", {"categories": categories, "vips": vips})


def search(request):
    if request.method == "POST":
        _search = request.POST.get("search", "")
        _items = models.Item.objects.all().filter(is_active=True, title__icontains=_search)
        return render(request, "ItemListPage.html", context={"items": _items})


def item_list(request):
    items = models.Item.objects.all().filter(is_active=True).order_by("-price", "-title")
    return render(request, "ItemListPage.html", context={"items": items})


def category(request):
    categories = models.CategoryItem.objects.all()
    return render(request, "CategoryPage.html", {"categories": categories})


def items(request, slug_name: str):
    cat = models.CategoryItem.objects.get(slug=slug_name)
    # items = отдельные сущности
    _items = models.Item.objects.all().filter(is_active=True, category=cat)

    return render(request, "ItemListPage.html", context={"items": _items})


def item(request, item_id: str):
    """
    Плюсы логики во View - единственная ответственность.
    """

    _item = models.Item.objects.get(id=int(item_id))
    _comments = _item.get_all_comments()
    _bugs_count = models.ItemBug.objects.filter(item=_item).count()

    selected_page = request.GET.get(key="page", default=1)
    page_objs = Paginator(object_list=_comments, per_page=4)
    page_obj = page_objs.page(number=selected_page)

    context = {
        "item": _item,
        "page_obj": page_obj,
        "total_rating_value": _item.total_rating(),
        "is_my_rating": _item.is_my_rating_selection(user=request.user),
        "v_bugs_count": _bugs_count,
    }

    return render(
        request,
        "ItemDetailPage.html",
        context=context,
    )


def bug(request, item_id: str):
    _item = models.Item.objects.get(id=int(item_id))
    _author = request.user  # django auth

    try:
        models.ItemBug.objects.get(author=_author, item=_item)
    except Exception as _:
        models.ItemBug.objects.create(author=_author, item=_item)

    return redirect(reverse("item", args=(item_id,)))


def comment(request):
    if request.method == "POST":
        text = request.POST.get("text", "")
        article_id = request.POST.get("article", "")
        _item = models.Item.objects.get(id=int(article_id))
        models.CommentItem.objects.create(author=request.user, article=_item, text=text)
        return redirect(reverse("item", args=(article_id,)))


def comment_delete(request, comment_id: str, item_id: str):
    models.CommentItem.objects.get(id=int(comment_id)).delete()
    return redirect(reverse("item", args=(item_id,)))


def rating(request, item_id: str, is_like: str):
    author = request.user
    _item = models.Item.objects.get(id=int(item_id))
    _is_like = True if is_like == "1" else False

    """
# ничего нет -> like -> ItemRating.objects.create(is_like=True)
# ничего нет -> dislike -> ItemRating.objects.create(is_like=False)
# is_like=True -> like -> ItemRating.objects.delete()
# is_like=False -> dislike -> ItemRating.objects.delete()
# is_like=True -> dislike -> is_like=False
# is_like=False -> like -> is_like=True
    """

    try:
        # пытаюсь взять от этого пользователя к этому товару лайк или дизайн, если нет - ошибка
        like_obj = models.ItemRating.objects.get(author=author, item=_item)
        # если я раньше поставил лайк и сейчас снова жму лайк, то удалить запись
        if like_obj.is_like and _is_like:
            like_obj.delete()
        # если я раньше поставил дизлайк и сейчас снова жму дизлайк, то удалить запись
        elif not like_obj.is_like and not _is_like:
            like_obj.delete()
        # если я раньше поставил не тоже, что и сейчас, то обновляю запись
        else:
            like_obj.is_like = _is_like
            like_obj.save()
    except Exception as _:
        # создаю запись, если такой записи нет
        like_obj = models.ItemRating.objects.create(author=author, item=_item, is_like=_is_like)

    return redirect(reverse("item", args=(item_id,)))


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


def test(request):
    """
    context_processors - контекстный процессор -
    функции, которые вызываются КАЖДЫЙ ВЫЗОВ render(...)
    """

    return render(request, "TestPage.html")
