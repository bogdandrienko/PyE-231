import math
import random

from django.shortcuts import render
from django_app import models
from django.core.paginator import Paginator


def home(request):
    return render(request, 'Home.html')


def native_paginate(request, object_list, per_page):
    selected_page = request.GET.get(key='page', default=1)
    page_objs = Paginator(object_list=object_list, per_page=per_page)
    page_obj = page_objs.page(number=selected_page)
    return page_obj


def prices(request):
    data = [
        {"id": x, "title": f"Доставка животных {x}", "description": f"безопасно {x}", "price": 2600}
        for x in range(1, 100 + 1)
    ]
    # TODO - ЮНИКОД
    # sorting - порядок -
    data = sorted(data, key=lambda x: int(str(x["description"]).split(" ")[1]), reverse=True)
    context = {"page_obj": native_paginate(request, data, 7)}
    return render(request, 'Prices.html', context=context)


def animals(request):
    # берём из пути "http://127.0.0.1:8000/animals/?page=2&search=10"
    selected_page = request.GET.get(key='page', default=1)  # query params

    # берём из базы все объекты
    ans = models.Price.objects.all()  # QuerySet lazy (лениво - не берёт лишние)

    # генерируем экземпляр пагинатора
    page_objs = Paginator(object_list=ans, per_page=30)

    # берём выбранную страницу
    page_obj = page_objs.page(number=selected_page)

    return render(request, 'Animals.html', context={"page_obj": page_obj})


def generate(request):
    choices = ["медведь", "волк", "лиса"]
    for i in range(1, 100):
        models.Price.objects.create(title=f"{random.choice(choices)} {i}", description=f"Описание {100 - i}", price=i + 10000)
    return render(request, 'Home.html')
