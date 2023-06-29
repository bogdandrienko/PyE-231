from tkinter import Tk, Button
import random
import multiprocessing
import requests
import time

url = "https://picsum.photos/320/240/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


def sync_download_one_image():
    response = requests.get(url=url, headers=headers)
    with open(f"temp/image{random.randint(1, 10000000)}.jpg", "wb") as opened_file:
        opened_file.write(response.content)


def processing_download_mass_image():
    start_time = time.perf_counter()
    process_list = []
    for i in range(1, 9 + 1):
        process_list.append(multiprocessing.Process(target=sync_download_one_image, args=(), kwargs={}))
    for process in process_list:
        process.start()
    for process in process_list:
        process.join()
    print(f'Задача закончила работу за {round(time.perf_counter() - start_time, 5)}')


if __name__ == '__main__':
    window = Tk()
    window.title("Загрузчик картинок")
    window.geometry('300x150')

    # Кнопка для мультипроцессорной загрузки
    save_button = Button(window, text="Мультипроцессорная загрузка", command=processing_download_mass_image)
    save_button.pack()

    window.mainloop()
    input("press any key to close window")
