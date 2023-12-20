from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.cache import cache_page

from django_profiles import models


# Create your views here.


@cache_page(10)
def resume_form(request):
    if request.method == "GET":
        return render(request, "resume_form.html")


"""
print(request.POST)
# with open("database/users.txt", "a", encoding="utf-8") as f:
#     f.write(f"{iin}\n")

# RAW SQL - сырой SQL
# минусы: устаревший язык и синтаксис,
# специализация(неудобные исключения и циклы),
# разница диалектов(90% - PLSQL, MySQL, MSSQL, SQLITE, Oracle, PostgreSQL)
# плюсы:
# +скорость

# ORM - django ORM(SQLAlchemy, Tortoise)
# плюсы:
# скорость разработки
# универсальная: 99,9% логики для всех SQL одинаковы
# python-like (ООП стиль) и красота
# минусы:
# -скорость

# Golang (x100) + SQL

# Django ORM TODO INSERT
# profile.iin = "123"
# profile.save()
# if profile.id % 2 == 0:
#     profile.delete()
print(profile)
"""


def save_form(request):
    iin = request.POST["iin"]
    exp = request.POST["exp"]
    name = request.POST["name"]
    models.Profile.objects.create(iin=iin, exp=exp, name=name)  # models.Profile.objects.bulk_create([])  # пачка
    return redirect(reverse("resume_form"))


"""
objs = models.Profile.objects.all()  # получить все
# objs.filter(iin__icontains="")  # поиск (WHERE iin LIKE %S%)
# objs.filter(exp=5)  # фильтрация (WHERE exp = '5')
# objs.order_by('-exp', 'iin')  # сортировка (ORDER BY exp DESC, iin ASC)
for i in obj:
    if i.exp > 3:
        print("ОПЫТНЫЙ!")
"""


def profiles(request):
    obj = models.Profile.objects.all().filter(is_active=True)
    return render(request, "profiles.html", {"profiles": obj})


def profile(request, pk: str):
    obj = models.Profile.objects.get(id=int(pk))
    return render(request, "profile.html", {"profile": obj})


def profile_delete(request, pk: str):
    obj = models.Profile.objects.get(id=int(pk))
    obj.is_active = False
    obj.save()  # obj.delete()
    return redirect(reverse("profiles"))
