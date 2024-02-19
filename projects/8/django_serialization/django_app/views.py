import datetime
import json

from django.contrib.auth.models import User
from django.http import JsonResponse, HttpRequest
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from django_app import models, serializers


def api_native(request: HttpRequest) -> JsonResponse:
    books = models.Book.objects.all()  # 10.000.000
    # <class 'django.db.models.query.QuerySet'> <QuerySet [<Book: Book object (1)>, <Book: Book object (2)>]>
    print(type(books), books)

    # books = books.filter(title__icontains="12414314")
    # books = books.filter(description__endswith="1413434")
    # for book in books:
    #     print(book.title)

    # <class 'django_app.models.Book'> Book object (1)
    book1 = books[0]
    print(type(book1), book1,  book1.description)

    """
    Питоновский (Python like object) - нельзя передать напрямую.
    
    Python -> Json (сериализация - serialization)
    """
    dict1 = {"Name": "Java"}
    print(type(dict1), dict1)  # <class 'dict'> {'Name': 'Java'}
    # dict1_json = json.dump()  # записывает в файл
    dict1_json = json.dumps(dict1)
    print(type(dict1_json), dict1_json)  # <class 'str'> '{"Name": "Java"}'
    print(type(dict1_json), dict1_json)  # <class 'str'> '12'

    # JSON - 92%
    # XML - 1-2%
    #  - %

    """
    {"id": 1, "title": "Книга 1", "description": "Описание 1", "file": "/static/pdf/book1.pdf"}
    
    {"books": [
        {"id": 1, "title": "Книга 1", "description": "Описание 1", "file": "/static/pdf/book1.pdf"},
        {"id": 2, "title": "Книга 2", "description": "Описание 2", "file": "/static/pdf/book2.pdf"}
    ]}
    """

    # 1. Ленивая подгрузка картинки -
    """Кэш. Страница будет отображаться, картинка может прийти позже."""

    # 2. Ленивый(генератор) значений -

    # target = 78
    # не ленивый - весь код будет вычисляться
    # cars = [x+2*2 for x in range(1, 1000000)]
    # for i in cars:
    #     if i == target:
    #         return True
    #
    # def get_car(j):
    #     yield j+2*2
    # cars = (get_car(x) for x in range(1, 1000000))  # gen obj
    # for i in cars:
    #     if i == target:
    #         return True

    # 3. QuerySet - ленивый запрос, т.е. пока нет прямого обращения к данным, запрос не выполняется

    """Причина отсутвия автоматической сериализации - сложность и вложенность
    (какие поля брать/не брать, какие поля во что превращать, сверх сложные структуры)
    """
    book1_json = {
        "id": book1.id,
        "title": book1.title,
        "description": book1.description,
        "file": "/static/pdf/book1.pdf"
    }


    # беру все книги
    books = models.Book.objects.all()
    # беру первую книгу
    book = books[0]
    # ручная(гибкая) сериализация в JSON
    book1_json = {
        "id": book.id,
        "title": book.title,
        "full_name": book.title + " " + book.description,  # generic / вычисляемое поле
        # "description": book.description,
        "file": "/static/pdf/book1.pdf"
    }
    # Отправка ответа к frontend-у

    return JsonResponse(data={"message": book1_json})


@api_view(http_method_names=["GET"])
def api(request: Request) -> Response:
    book_obj = models.Book.objects.all()[0]
    book_json = serializers.BookSerializer(instance=book_obj, many=False).data
    return Response(
        data={"message": book_json, "book_id": book_obj.id}
    )

@api_view(http_method_names=["GET"])
def api_users(request: Request) -> Response:
    users_objs = User.objects.all()
    users_json = serializers.UserSerializer(instance=users_objs, many=True).data
    return Response(
        data={"data": users_json, "time": str(datetime.datetime.now())}
    )
