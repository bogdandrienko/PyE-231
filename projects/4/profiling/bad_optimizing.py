import random
import sys
import time


# import memory_profiler
# mprof run --include-children python bad_optimizing.py
# mprof plot --output bas_optimizing.png

# pip install memory_profiler
# pip install matplotlib

# @memory_profiler.profile
def start():



    cars = []  # todo СТРУКТУРА ДАННЫХ "ЛИСТ" вся хранится в оперативной памяти!
    for i in range(1, car_count + 1):
        new_car = {
            "id": i,
            "name": random.choice(car_names),
            "color": random.choice(car_colors)
        }
        cars.append(new_car)












    # for j in cars:
    #     print(j)

    # 24 * 60 * 60
    # ~ 100 000
    # 3 000 000 * 500
    # 150 000 000
    print(round(sys.getsizeof(cars) / 1024 / 1024, 1), "megabytes")
    return cars


if __name__ == "__main__":
    time_start = time.perf_counter()











    car_names = ["Toyota", "Honda", "Audi", "Nissan"]
    car_colors = ["Black", "Blue", "Red", "Yellow", "White"]
    car_count = 50000000















    # сборщик мусора (GC) - замедляет работу кода, но упрощает работу работу с паматью
    # (Python, PHP, JavaScript, Java, Go, C#) vs (C++, Rust, C, Assembler)

    cars_arr = start()
    with open("bad.txt", "w", encoding="utf-8") as file:
        for car in cars_arr:
            file.write(f'{car["id"]} | {car["name"]} |{car["color"]}\n')

    print(round(sys.getsizeof(cars_arr), 1), "bytes")
    print(round(time.perf_counter() - time_start, 3), "s elapsed time")
