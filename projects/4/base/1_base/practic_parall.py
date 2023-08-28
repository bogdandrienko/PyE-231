import random
import time
import requests
import threading


def ex():
    print("Hi")
    time.sleep(3.0)  # блокирующий код
    print("Bye")

    start = time.perf_counter()
    response = requests.get(
        "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
    print(response.status_code)
    print(f"elapsed time: ", round(time.perf_counter() - start, 7))


from tkinter import *


def data():
    index = 1
    while True:
        time.sleep(0.1)
        print(index)
        index += 1
        label.config(text=f"index: {index}")
        if index == 30:
            break


def data2():
    url = "https://picsum.photos/320/240/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }

    def sync_download_one_image():
        response = requests.get(url=url, headers=headers)
        with open(f"temp2/image{random.randint(1, 10000000)}.jpg", "wb") as opened_file:
            opened_file.write(response.content)

    sync_download_one_image()

def start():
    new_thread = threading.Thread(target=data2)
    new_thread.start()


root = Tk()  # создаем корневой объект - окно
root.title("Приложение на Tkinter")  # устанавливаем заголовок окна
root.geometry("300x250")  # устанавливаем размеры окна

label = Label(text="Hello METANIT.COM")  # создаем текстовую метку
label.pack()  # размещаем метку в окне
btn = Button(text="Hello METANIT.COM", command=data2)  # создаем текстовую метку
btn.pack()  # размещаем метку в окне

root.mainloop()

# Последовательное выполнение задач:
# блокирование потока
# Вы готовите омлет, и только после завершения приготовления ставите на плиту чайник

# Масштабирование задач:(против блокирующего кода)
# Параллельное выполнение задач (полный параллелизм - только если ядро занимается только своей одной задачей)
# Вы зовёте второго человека следить за чайником
# - нельзя купить много ядер

# Конкурентное выполнение задач
# Быстрое переключение между несколькими задачами
# - переключение между задачами не бесплатное - "смена контекста"
# - слишком большое количество задач ведёт к парадоксу - ядро "переключается между задачами, спрашивает их статус, но не успевает их делать"

# Асинхронное выполнение задач(подвид конкурентного)
# Мы поставили чайник, и готовим омлет(queue - очередь), пока чайник не "засвистит".

