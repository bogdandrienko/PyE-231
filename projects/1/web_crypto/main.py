import datetime
import time
import requests


def get_data():
    # todo Получение "сырых" данных
    url = "https://api.binance.com/api/v3/ticker/price?"
    data_raw = requests.get(url=url)

    # todo Проверка на положительный ответ
    if int(data_raw.status_code) == 200:  # 200 - ok, 201 - created, 400+ ошибка клиента, 500+ ошибка серверка
        valutes = data_raw.json()
        # print(valutes)

        # todo Фильтрация массива на больше 10000.0
        data_clear = []
        for valute in valutes:
            if float(valute["price"]) > 10000.0:
                data_clear.append(valute)
        # print(data_clear)

        # todo Сортировка массива "по возрастанию"
        data_asc = sorted(data_clear, key=lambda x: x["price"], reverse=True)
        # print(data_asc)

        # todo "Форматированный" вывод на экран
        with open("data.txt", "w") as file:
            for i in data_asc:  # list[dict]
                txt = f"{i['symbol']} | {i['price']}"
                print(txt)
                file.write(txt + "\n")
        print(datetime.datetime.now())
    else:
        print(data_raw.status_code)


if __name__ == "__main__":
    while True:
        try:
            time_start = time.perf_counter()
            get_data()
            time_end = time.perf_counter()
            elapsed = round(time_end-time_start, 1)  # 0.8
            if elapsed >= 3.0:
                continue
            else:
                time.sleep(3.0-elapsed)
        except Exception as error:
            print(error)
