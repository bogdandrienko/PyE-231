########################################################################################################################
# TODO потоки исполнения

import time
import random
import threading
import multiprocessing
import asyncio
import requests
import aiohttp

import time

# print(1)
# time.sleep(1.5)
# print(2)

# конкурентность - "фейковый" параллелизм,
# 1s = | 0.005 ms ставит чайник | 0.002 тратит на переключение | 0.012 ms жарит яйца | 0.002 тратит на переключение | | 0.005 ms ставит чайник | 0.002 тратит на переключение | 0.012 ms жарит яйца | 0.002 тратит на переключение

# 8 ядер - настоящий параллелизм,

# todo блокирующая
# for i in range(1, 5 + 1):
#     p = requests.get('https://upload.wikimedia.org/wikipedia/commons/a/a2/Python_royal_35.JPG')
#     with open(f"temp/img{i}.jpg", "wb") as f:
#         # time.sleep(3.0)
#         f.write(p.content)
# todo блокирующая

# print(3)

# sync VS async VS threading VS multiprocessing

# sync =                1 процесс: 1 поток
# threading =           1 процесс: N поток
# multiprocessing =     N процесс: N поток
# async =               1 процесс: 1 поток

url = "https://picsum.photos/320/240/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


def sync_download_one_image():
    response = requests.get(url=url, headers=headers)
    with open(f"temp/image{random.randint(1, 10000000)}.jpg", "wb") as opened_file:
        opened_file.write(response.content)
    # time.sleep(0.1)
    # time.sleep(5.1)


def sync_download_mass_image():
    start_time = time.perf_counter()

    # обычный вид
    # sync_download_one_image()
    # sync_download_one_image()
    # sync_download_one_image()

    # загрузка 10 картинок в этом потоке
    for i in range(1, 1 + 1):
        sync_download_one_image()

    print(f'Задача закончила работу за {round(time.perf_counter() - start_time, 5)}')


def threading_download_mass_image():
    start_time = time.perf_counter()

    # загрузка одной картинки в дополнительном потоке
    # thread = threading.Thread(target=sync_download_one_image, args=(), kwargs={})  # формирование задачи
    # thread.start()
    # thread.join()

    # thread_1 = threading.Thread(target=sync_download_one_image, args=(), kwargs={})  # формирование задачи
    # thread_2 = threading.Thread(target=sync_download_one_image, args=(), kwargs={})  # формирование задачи
    # thread_3 = threading.Thread(target=sync_download_one_image, args=(), kwargs={})  # формирование задачи
    #
    # thread_1.start()
    # thread_2.start()
    # thread_3.start()
    #
    # thread_1.join()
    # thread_2.join()
    # thread_3.join()

    # time.sleep(0.1)

    # загрузка 10 картинок в дополнительных 10 потоках
    thread_list = []
    for i in range(1, 100 + 1):
        thread_list.append(threading.Thread(target=sync_download_one_image, args=(), kwargs={}))
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()

    print(f'Задача закончила работу за {round(time.perf_counter() - start_time, 5)}')


def processing_download_mass_image():
    start_time = time.perf_counter()

    # загрузка одной картинки в дополнительном процессе
    # process = multiprocessing.Process(target=sync_download_one_image, args=(), kwargs={})  # формирование задачи
    # process.start()
    # process.join()

    # process_1 = multiprocessing.Process(target=sync_download_one_image, args=(), kwargs={})  # формирование задачи
    # process_2 = multiprocessing.Process(target=sync_download_one_image, args=(), kwargs={})  # формирование задачи
    # process_3 = multiprocessing.Process(target=sync_download_one_image, args=(), kwargs={})  # формирование задачи
    #
    # process_1.start()
    # process_2.start()
    # process_3.start()
    #
    # process_1.join()
    # process_2.join()
    # process_3.join()

    # time.sleep(0.1)

    # загрузка 10 картинок в дополнительных 10 потоках
    process_list = []
    for i in range(1, 100 + 1):
        process_list.append(multiprocessing.Process(target=sync_download_one_image, args=(), kwargs={}))
    for process in process_list:
        process.start()
    for process in process_list:
        process.join()

    print(f'Задача закончила работу за {round(time.perf_counter() - start_time, 5)}')


if __name__ == "__main__":
    # sync_download_mass_image()            # 1x = 0.10079  |   10x = 1.00508   |   100x = 10.04395
    # threading_download_mass_image()       # 1x = 0.10102  |   10x = 0.10145   |   100x = 0.10767
    # processing_download_mass_image()      # 1x = 0.32884  |   10x = 0.45594   |   100x = 3.22451
    async_task()

    pass
