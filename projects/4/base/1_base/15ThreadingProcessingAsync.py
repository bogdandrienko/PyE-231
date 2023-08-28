########################################################################################################################
# TODO потоки исполнения
import concurrent.futures
import time
import random
import threading
import multiprocessing
import asyncio
import requests  # synchronous
import aiohttp  # asynchronous
# import aiofiles  # open() -- sync  | aiofiles.open() -- async
# import aiogram
# import aiopg  # psycopg2 -- sync | aiopg.open() -- async
# import aiosqlite
import requests
import time





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
















# print(1)
# print(2)
#
# # todo блокирующая
# for i in range(1, 5+1):
#     p = requests.get('https://upload.wikimedia.org/wikipedia/commons/a/a2/Python_royal_35.JPG')
#     with open(f"temp/img{i}.jpg", "wb") as f:
#         # time.sleep(3.0)
#         f.write(p.content)
# # todo блокирующая
#
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
    time.sleep(1.0)
    # response = requests.get(url=url, headers=headers)
    # with open(f"temp2/image{random.randint(1, 10000000)}.jpg", "wb") as opened_file:
    #     opened_file.write(response.content)


def sync_download_mass_image():
    start_time = time.perf_counter()

    # загрузка одной картинки в этом потоке
    # sync_download_one_image()

    # обычный вид
    # sync_download_one_image()
    # sync_download_one_image()
    # sync_download_one_image()
    # sync_download_one_image()
    # sync_download_one_image()

    # загрузка 10 картинок в этом потоке
    for i in range(1, 10 + 1):
        sync_download_one_image()

    print(f'Задача закончила работу за {round(time.perf_counter() - start_time, 5)}')


def threading_download_mass_image():
    start_time = time.perf_counter()

    # загрузка одной картинки в дополнительном потоке
    # thread = threading.Thread(target=sync_download_one_image, args=(), kwargs={})  # формирование задачи
    # thread.start()  # запуск задачи
    # thread.join()  # ожидание завершения потока

    # обычный вид
    # thread_1 = threading.Thread(target=sync_download_one_image, args=())
    # thread_1.start()
    #
    # thread_2 = threading.Thread(target=sync_download_one_image, args=())
    # thread_2.start()
    #
    # thread_3 = threading.Thread(target=sync_download_one_image, args=())
    # thread_3.start()
    #
    # thread_1.join()
    # thread_2.join()
    # thread_3.join()

    # загрузка 10 картинок в дополнительных 10 потоках
    thread_list = []
    for i in range(1, 10 + 1):
        thread_list.append(threading.Thread(target=sync_download_one_image, args=(), kwargs={}))
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()

    # загрузка 10 картинок в дополнительных 10 процессах в 1 потоке, но с ограничением на 10 потоков
    # with concurrent.futures.ThreadPoolExecutor(max_workers=16*2+1) as executor:
    #     for i in range(1, 9+1):
    #         executor.submit(sync_download_one_image, ())

    # возврат результатов
    # with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    #     futures = []
    #     for url in range(1, 10+1):
    #         futures.append(executor.submit(sync_download_one_image))
    #     for future in concurrent.futures.as_completed(futures):
    #         print(future.result())
    # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    #     futures = []
    #     for i in range(1, 10+1):
    #         future = executor.submit(sync_download_one_image)
    #         futures.append(future.result())

    print(f'Задача закончила работу за {round(time.perf_counter() - start_time, 5)}')


def processing_download_mass_image():
    start_time = time.perf_counter()

    # загрузка одной картинки в дополнительном процессе в 1 потоке
    # process = multiprocessing.Process(target=sync_download_one_image, args=(), kwargs={})  # формирование задачи
    # process.start()  # запуск задачи
    # process.join()  # ожидание завершения потока

    # обычный вид
    # process_1 = multiprocessing.Process(target=sync_download_one_image, args=())
    # process_1.start()
    #
    # process_2 = multiprocessing.Process(target=sync_download_one_image, args=())
    # process_2.start()
    #
    # process_3 = multiprocessing.Process(target=sync_download_one_image, args=())
    # process_3.start()
    #
    # process_1.join()
    # process_2.join()
    # process_3.join()

    # загрузка 10 картинок в дополнительных 10 процессах в 1 потоке
    process_list = []
    for i in range(1, 100 + 1):
        process_list.append(multiprocessing.Process(target=sync_download_one_image, args=(), kwargs={}))
    for process in process_list:
        process.start()
    for process in process_list:
        process.join()

    # загрузка 10 картинок в дополнительных 10 процессах в 1 потоке, но с ограничением на 10 процессов
    # with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
    #     for i in range(1, 10+1):
    #         executor.submit(sync_download_one_image, ())

    print(f'Задача закончила работу за {round(time.perf_counter() - start_time, 5)}')


async def async_t():
    await asyncio.sleep(1.0)
    # time.sleep(1.0)  # todo SYNC!

    # async with aiohttp.ClientSession() as session:
    #     async with session.get(url=url, headers=headers) as response:
    #         data = await response.read()
    #
    #         with open(f"temp2/image{random.randint(1, 10000000)}.jpg", "wb") as opened_file:
    #             opened_file.write(data)


def async_task():
    start_time = time.perf_counter()

    # загрузка одной картинки
    # asyncio.run(async_t())

    async def async_task_asyncio():  # coroutine(promise)
        list_async = []
        for _ in range(1, 1000+1):
            list_async.append(async_t())
        await asyncio.gather(asyncio.gather(*list_async))

    asyncio.run(async_task_asyncio())

    print(f'Задача закончила работу за {round(time.perf_counter() - start_time, 5)}')


if __name__ == "__main__":
    # sync_download_mass_image()            # 1x == 1.00      |  10x = 10.00       | 100x = 100.00 s      | too long
    # threading_download_mass_image()       # 1x == 1.00      |  10x = 1.00        | 100x = 1.00  s       | 1000x = 1.00 s
    # processing_download_mass_image()      # 1x == 1.28      |  10x = 1.47        | 100x = 4.29  s       | too expensive
    async_task()                            # 1x == 1.00      |  10x = 1.00        | 100x = 1.00 s        | 1000x = 1.01

    pass

########################################################################################################################
