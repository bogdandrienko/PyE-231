import datetime
import random
import requests
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')


class Docs:
    """Основная документация"""

    # URL(route) -> VIEW(def) -> MODELS(database) -> TEMPLATE(html)

    # MVC(MVT) - Model View Controller (Template)
    # MVC(T) <<< React or View

    # https://flask.palletsprojects.com/en/2.3.x/

    # home page - ссылки, новости, футер, о нас
    # about page
    # contacts page

    # ratings page
    # search page

    # public page

    # pricing  ->
    class Price:  # сущность - ТАБЛИЦА В БАЗЕ ДАННЫХ
        id: int   # 1
        title: str  # Коронки
        description: str  # Мы Вам можем предложить на выбор корейские и немецкие...
        price_low: float  # 120 000
        price_high: float  # 350 000
        image: str  # /img/example/коронки.jpg


class Views:
    class Base:
        @staticmethod
        @app.route("/index")
        def index():
            return f"<h1>Index Page {datetime.datetime.now()}</h1>"

        @staticmethod
        @app.route("/")
        def home():
            return render_template('home.html')

        @staticmethod
        @app.route("/about")
        def about():
            return render_template('about.html')

    class Books:
        @staticmethod
        @app.route("/ratings/top")  # URL
        def ratings_top():  # VIEW

            books: list[dict] = [{
                "id": x,
                "title": f"451° по Фаренгейту {x}",
                "image": "img/error.jpg",
                "description": """
Мастер мирового масштаба, совмещающий в литературе несовместимое. Создатель таких ярчайших шедевров, как 
"Марсианские хроники", "451° по Фаренгейту", "Вино из одуванчиков" и так далее и так далее. Лауреат многочисленных 
премий. Это Рэй Брэдбери. Его увлекательные истории прославили автора не только как непревзойденного рассказчика, 
но и как философа, мыслителя и психолога. Магический реализм его прозы, рукотворные механизмы радости, переносящие 
человека из настоящего в волшебные миры детства, чудо приобщения к великой тайне Литературы, щедро раздариваемое 
читателю, давно вывели Брэдбери на высокую классическую орбиту. Собранные в этой книге произведения - достойное 
тому подтверждение."""[:70],
                "authors": [{"id": 1, "name": f"Рэй Брэдбери {x}"}],
                "categories": [{"id": 1, "name": "Проза"}, {"id": 2, "name": "Проза 2"}],
            } for x in range(1, 100)]  # MODEL
            name = "Роман"
            todos: list[dict] = requests.get("https://jsonplaceholder.typicode.com/todos").json()  # MODEL

            return render_template(template_name_or_list='ratings_top.html', name=name, books=books, todos=todos)  # TEMPLATE

    class Api:
        @staticmethod
        @app.route("/api")
        def api():
            data = [
                {
                    "userId": 1,
                    "id": 1,
                    "title": "delectus aut autem",
                    "completed": False
                },
                {
                    "userId": 1,
                    "id": 2,
                    "title": "quis ut nam facilis et officia qui",
                    "completed": False
                },
                {
                    "userId": 1,
                    "id": 3,
                    "title": "fugiat veniam minus",
                    "completed": False
                }]
            return {"status": "OK", "message": data}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
