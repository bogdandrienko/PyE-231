import datetime
import random
import re

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View, ListView, DetailView, DeleteView, CreateView

from django_app import models, utils

"""
Классы - ООП.
1. Расширяемость(наследуемость), т.е. можно писать меньше кода, если правильно выстроить иерархию наследования.
Есть определённые блоки кода, которые очень часто повторяются - их можно вынести на более высокий уровень абстракции.
2. Возможность доработки.
!СЛОЖНЕЕ

from django.views.generic GENERIC - уже готовые шаблоны для большинства ситуаций

path("about/", TemplateView.as_view(template_name="about.html"))

Миксины(mixins) - смесь нескольких классов     
class TemplateView(TemplateResponseMixin, ContextMixin, View):

class GetObject(View): - получает один объект
class GetObject(View, LoginRequired): - получает один объект, но требует авторизацию
class GetObject(View, LoginRequired, Pagination, Cache): - получает один объект, но требует авторизацию, включает пагинацию и кэш
class GetObject(View, LoginRequired, IsAdmin): - получает один объект, но требует авторизацию и права админа

Функции - Функциональное/процедурное.
1. Гибкость
минус - много кода
"""


class AboutView(TemplateView):
    template_name = "about.html"


def about(request):
    return render(request, "about.html")


class ProfileView(View):
    template_name = "profile.html"

    def get(self, request):
        """Будет возвращать объект профиля пользователя"""
        # profile = models.Profile.objects.get(user=request.user)
        # profile = request.user.profile  # autojoin - вытащить запись по связи
        return render(request, template_name=self.template_name)

    def post(self, request):
        """Будет обновлять профиль"""
        avatar = request.FILES.get("avatar", None)  # UploadInMemoryFile
        if avatar:
            request.user.profile.avatar = avatar
            request.user.profile.save()
        return render(request, template_name=self.template_name)


def home(request):
    # print(request.META)
    categories = utils.get_cache(key="categories", query=lambda: models.CategoryItem.objects.all(), timeout=3)

    selected_page = request.GET.get(key="page", default=1)
    page_objs = Paginator(object_list=categories, per_page=3)
    page_obj = page_objs.page(number=selected_page)

    vips = utils.get_cache(
        key="vips",
        query=lambda: models.Vip.objects.all().filter(expired__gt=datetime.datetime.now()).order_by("priority", "-article"),
        timeout=1,
    )
    return render(request, "HomePage.html", {"page_obj": page_obj, "vips": vips})


def ratings(request):
    # FRONTEND(USER) -> VIEW

    # _items = utils.get_cache(key="ratings", query=lambda: models.Item.objects.filter(is_active=True, is_moderate=True), timeout=3)
    _items = models.Item.objects.filter(is_active=True, is_moderate=True)
    sort = request.GET.get("sort", "desc")
    match sort:
        case "asc":
            _items = sorted(_items, key=lambda x: (x.total_rating(), x.title), reverse=False)
        case "desc":
            _items = sorted(_items, key=lambda x: (x.total_rating(), x.title), reverse=True)
        case "date_asc":
            _items = sorted(_items, key=lambda x: (x.date, x.title), reverse=False)
        case "date_desc":
            _items = sorted(_items, key=lambda x: (x.date, x.title), reverse=True)
        case _:
            _items = sorted(_items, key=lambda x: x.title, reverse=False)

    return render(request, "RatingsPage.html", {"items": _items, "sort": sort})


def search(request):
    if request.method == "POST":
        _search = request.POST.get("search", "")
        _items = models.Item.objects.filter(is_active=True, is_moderate=True, title__icontains=_search)
        return render(request, "ItemListPage.html", context={"items": _items, "search": _search})


def item_list(request):
    _items = models.Item.objects.filter(is_active=True, is_moderate=True).order_by("-price", "-title")
    return render(request, "ItemListPage.html", context={"items": _items})


def category(request):
    categories = models.CategoryItem.objects.all()
    return render(request, "CategoryPage.html", {"categories": categories})


def f_items(request, slug_name: str):
    cat = models.CategoryItem.objects.get(slug=slug_name)
    # items = отдельные сущности
    _items = models.Item.objects.filter(is_active=True, is_moderate=True, category=cat)

    """
/*
cat = models.CategoryItem.objects.get(slug=slug_name)
_items = models.Item.objects.filter(is_active=True, is_moderate=True, category=cat)
*/

/*
SELECT * FROM public.django_app_item
WHERE category_id in (
	SELECT id from public.django_app_categoryitem
	where slug = 'electro'	
) AND is_active = 'true'
*/

/*
SELECT t1.*, t2.title as category_name FROM public.django_app_item as t1
inner join public.django_app_categoryitem as t2 
	ON t1.category_id = t2.id
WHERE t2.slug = 'electro' AND t1.is_active = 'true'
*/
    """

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


def public(request):
    if request.method == "GET":
        _categories = models.CategoryItem.objects.all()
        return render(request, "PublicPage.html", context={"categories": _categories})
    elif request.method == "POST":
        title = str(request.POST["title"])
        description = str(request.POST["description"])
        price = int(request.POST["price"])
        _category = models.CategoryItem.objects.get(slug=str(request.POST["category"]))

        avatar = request.FILES.get("avatar", None)  # UploadInMemoryFile
        file = request.FILES.get("file", None)

        _item = models.Item.objects.create(
            title=title, description=description, price=price, category=_category, avatar=avatar, file=file, is_active=True, is_moderate=False
        )

        return redirect(reverse("category"))


def update_item(request, item_id: str):
    if request.method == "GET":
        _categories = models.CategoryItem.objects.all()
        _item = models.Item.objects.get(id=int(item_id))
        return render(request, "UpdatePage.html", context={"categories": _categories, "item": _item})
    elif request.method == "POST":
        title = str(request.POST["title"])
        description = str(request.POST["description"])
        price = int(request.POST["price"])
        _category = models.CategoryItem.objects.get(slug=str(request.POST["category"]))

        avatar = request.FILES.get("avatar", None)  # UploadInMemoryFile
        clear_avatar = True if request.POST.get("clear_avatar", None) else False
        file = request.FILES.get("file", None)

        _item = models.Item.objects.get(id=int(item_id))
        if _item.title != title:
            _item.title = title
        if _item.description != description:
            _item.description = description
        if _item.price != price:
            _item.price = price
        if _item.category != _category:
            _item.category = _category
        if clear_avatar:
            _item.avatar = None
        if avatar:
            _item.avatar = avatar
        if file:
            _item.file = file
        _item.save()

        return redirect(reverse("category"))


def item_hide(request, item_id: str):
    _item = models.Item.objects.get(id=int(item_id))
    _item.is_active = False
    _item.save()
    # отправить уведомление или письмо модератору
    return redirect(reverse("category"))


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
        # profile = models.Profile.objects.create(user=usr)

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


@csrf_exempt
def test(request):
    """
    context_processors - контекстный процессор -
    функции, которые вызываются КАЖДЫЙ ВЫЗОВ render(...)
    """
    if request.method == "POST":
        print(request.POST)
        data = [{"mes": f"{x}: {x**2}"} for x in range(1, 100)]
        return JsonResponse(data={"res": data}, status=211)

    return render(request, "TestPage.html")


def check_access_slug(slug: str, redirect_url: str = "home"):
    """Параметризируемый декоратор - конструктор декоратора"""

    def check_access(func):
        def wrapper(*args, **kwargs):
            user: User = args[0].user
            if not user.is_authenticated:
                return redirect(reverse(redirect_url))
            profile: models.Profile = user.profile
            is_access: bool = profile.check_access(slug)
            if not is_access:
                return redirect(reverse(redirect_url))
            # TODO VIEW
            res = func(*args, **kwargs)
            return res

        return wrapper

    return check_access


@check_access_slug(slug="UsersModeratePage_view")
def moderate_users(request):
    users = User.objects.all()
    return render(request, "ModerateUsers.html", context={"users": users})


@check_access_slug(slug="ItemsModeratePage_view")
def moderate_items(request):
    _items = models.Item.objects.filter(is_active=True, is_moderate=False)
    return render(request, "ModerateItems.html", context={"items": _items})


@check_access_slug(slug="UsersModeratePage_ban")
def moderate_ban_users(request):
    return render(request, "ModerateUsers.html")


@check_access_slug(slug="UsersModeratePage_delete")
def moderate_delete_users(request):
    return render(request, "ModerateUsers.html")


def chat(request):
    _rooms = models.Room.objects.all()[::-1]
    return render(request, "ChatPage.html", context={"rooms": _rooms})


@login_required
def room(request, room_slug: str):
    _room = models.Room.objects.get(slug=room_slug)
    _messages = models.Message.objects.filter(room=_room)[:30][::-1]
    return render(request, "RoomPage.html", context={"room": _room, "messages": _messages})


# /item/6/?new_status=delete
@check_access_slug(slug="ItemsModeratePage_success")
def moderate_item(request, item_id: str):
    # /item/6/?new_status=delete
    # /item/6/?new_status=success
    _new_status = request.GET["new_status"]
    _item = models.Item.objects.get(id=int(item_id))
    if _new_status == "success":
        _item.is_moderate = True
        _item.save()
    else:
        _item.delete()

    return redirect(reverse("moderate_items"))
