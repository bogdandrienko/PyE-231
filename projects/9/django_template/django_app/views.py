import random
import threading
import time

import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from django_app import utils, models, serializers


@utils.Decorators.constr_dec_logger(is_class=False)
def index_http(request):
    return HttpResponse("<h1>This is a Index Page</h1>")


@utils.Decorators.constr_dec_logger(is_class=False)
@utils.Decorators.dec_error_handle
def index_json(request):
    print(1 / 0)
    return JsonResponse(data={"response": "This is a Index Page"}, safe=False)


def react(request):
    return render(request, "build/index.html")


class Home(View):  # Mixins
    @utils.Decorators.constr_dec_logger(is_class=True)
    def get(self, request, *args, **kwargs):
        _contacts = models.Contact.objects.filter(is_completed=True)
        context = {"contacts": _contacts}
        return render(request, "home.html", context=context)

    def post(self, request, *args, **kwargs):
        models.Contact.objects.create(
            username=request.POST["username"],
            position=None,
            number=request.POST["number"],
            description=request.POST.get("description", ""),
        )
        return redirect(reverse("home"))


def contact_delete(request, contact_id: str):
    models.Contact.objects.get(id=int(contact_id)).delete()
    return redirect(reverse("home"))


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def get_contacts(request):
    if request.method == "GET":
        _contacts = models.Contact.objects.filter(is_completed=True)
        _contacts_json = serializers.ContactAllSerializer(_contacts, many=True).data
        return Response(data={"data": _contacts_json}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        print("request.data: ", request.data)
        return Response(data={"message": "успешно создано"}, status=status.HTTP_200_OK)


from django.core.cache import caches

ram_cache1 = caches["default"]


@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])
def test_cache(request):
    if request.method == "GET":

        _val = ram_cache1.get("test_cache")
        if _val is None:
            _val = random.randint(0, 10000000000)
            ram_cache1.set("test_cache", _val, 5)

        return Response(data={"data": _val}, status=status.HTTP_200_OK)


def without_celery(request):
    def log():
        """
        Плюс:
        * Задача в фоновом режиме

        Минусы:
        * Нагрузка, т.е. нельзя задачу делать в нужный
        * Планировщик - отсутвует функционал планировщика задач
        * Результат - нет отчёта о работе
        * Есть риск, что поток "упадёт" не отработав
        """
        # requests.post("http://127.0.0.1:8000/api/logger", json={"text": request.POST["text"], "count": 666, "is_hide": False})
        time.sleep(10)
        print("done")

    _t = threading.Thread(target=log)
    _t.start()
    # _t.join()
    return render(request, "Home.html")


from django_app import tasks as django_app_celery
from django_settings.celery import app as current_celery_app
from celery.result import AsyncResult


def celer(request):
    """
    python -m celery -A django_settings worker -l info
    """
    # oblako.kz

    # TODO start task
    # я нажимаю кнопку создать сервер
    # task_id = django_app_celery.add(10, 20)  # прямой вызов (не фоновая)
    task_id = django_app_celery.add.delay(10, 20)  # фоновый
    # c6f55087-2769-4df4-8945-244693faa416

    # 1 init
    # 2 send
    # 3 in progress(STARTED)
    # 4 completed(SUCCESS)
    # 5 failed
    return HttpResponse(f"<h1>Task_id: {task_id}</h1>")


def celer_res(request, res: str):
    # TODO GET RESULT FROM CELERY
    result = AsyncResult(res, app=current_celery_app)
    print(result.state)
    if result.state == "SUCCESS":
        res = f"{result.state} {result.get()}"
    else:
        res = f"{result.state} {None}"
    return HttpResponse(f"<h1>Task_id: {res} [{res}]</h1>")


@swagger_auto_schema(
    method="POST",
    request_body=serializers.PositionSerializer,  # Описание входных данных
    # manual_parameters=[
    #     openapi.Parameter("search_by", openapi.IN_QUERY, description="Поиск по этому параметру", type=openapi.TYPE_STRING, default="")
    # ],  # Описание входных данных
    responses={201: "Успех", 400: "Error detail"},  # Описание выходных данных
)
@api_view(http_method_names=["POST"])
def position_create(request: Request) -> Response:
    """
    Отправка формы с новой должностью.
    JSON -> DB
    """
    try:
        name = request.data["name"]  # json form
        models.Position.objects.create(name=name)  # ORM
        return Response(data={"message": "Успех"}, status=status.HTTP_201_CREATED)
    except Exception as error:
        return Response(data=f"ERROR: {error}", status=status.HTTP_400_BAD_REQUEST)
