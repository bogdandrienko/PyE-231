from flask import Flask, render_template
import json
import requests

app = Flask(__name__)


# @app.route("/")  # URL(маршрут)
# def hello_world():  # VIEW(контроллер)
#     return "Привет, Евгений!"

# @app.route("/")
# def hello_world():
#     name = "Роман"
#     # return "<p>Привет, Маулен!</p>"
#     return render_template('index.html', name=name)

@app.route("/")  # маршрут
def home():
    return render_template('home.html')  # template(шаблон, html)


@app.route("/pricing")
def pricing():
    price = 666

    # Указываете путь к вашему JSON файлу
    json_file_path = 'static/prices.json'
    # Открываем файл для чтения
    with open(json_file_path, 'r', encoding="utf-8") as file:
        # Загружаем данные из файла
        data: dict = json.load(file)
    # Теперь переменная data содержит данные из вашего JSON файла
    # print(data)

    old_data = data["data"]  # взятие значения из словаря
    print(type(old_data), old_data)
    for i in old_data:
        print(i)
    new_data = sorted(old_data, key=lambda x: x["name"])
    print("\n\n\n")
    for i in new_data:
        print(i)

    '''
{
'data': [
    {'id': 1, 'name': 'Кроссовки', 'price': 6500}, 
    {'id': 2, 'name': 'Рубашка', 'price': 4500}, 
    {'id': 3, 'name': 'Джинсы', 'price': 9500}, 
    {'id': 4, 'name': 'Кепка', 'price': 700}
    ]
}
    '''

    name = "Уалихан"
    count = 12
    questions = {"title": {"name": "Опросник"}}
    answers = [5, 4, 3, 2, 1]
    is_age = False
    return render_template('pricing.html', is_age=is_age, name="Уалихан", answers=answers, count=count, questions=questions, price=price,
                           new_data=new_data)


@app.route("/news")
def news():
    # 1. api - https://fakenews.squirro.com/news/sport
    # 2. parsing - web + bs4
    # 3. scrapping - selenium
    data = requests.get("https://fakenews.squirro.com/news/sport").json()

    # n1 = data.get('news', [])  # safe - если такого ключа нет, то верётся default
    # n2 = data['news']  # unsafe - если такого ключа нет, то возбуждается Exception
    # unsafe - используется, когда нужно вызывать ошибку при отсутствии ключа

    # username = request.GET['username']
    # username = request.GET.get('username', None)
    # if username is None:
    #     raise Exception("username not found")
    # password = request.GET["password"]
    # patronomyc = request.GET.get('patronomyc', "")

    # page = 1
    # text = data['text']
    # text = data.get('text', '')
    # https://hh.ru/search/vacancy?text=Python&area=6322&hhtmFrom=main&hhtmFromLabel=vacancy_search_line

    return render_template('news.html', news=data.get('news', []))


def get_safe(d: dict, key: str, default=None) -> any:
    try:
        return d[key]
    except KeyError:  # key not found
        return default


def hi():
    print("Hi, Уалихан!")


hi()
hi()
hi()
hi()
hi()
hi()
