import random
import sys
import time


# import memory_profiler
# mprof run --include-children python good_optimizing.py
# mprof plot --output good_optimizing.png

def start():
    for i in range(1, car_count + 1):
        new_car = {"id": i, "name": random.choice(car_names), "color": random.choice(car_colors)}
        yield new_car


if __name__ == "__main__":
    time_start = time.perf_counter()

    car_names = ["Toyota", "Honda", "Audi", "Nissan"]
    car_colors = ["Black", "Blue", "Red", "Yellow", "White"]
    car_count = 50000000  # 232

    # сборщик мусора (GC) - замедляет работу кода, но упрощает работу работу с паматью
    # (Python, PHP, JavaScript, Java, Go, C#) vs (C++, Rust, C, Assembler)

    # @memory_profiler.profile
    def start2():
        cars_arr = start()
        with open("good.txt", "w", encoding="utf-8") as file:
            for car in cars_arr:
                file.write(f'{car["id"]} | {car["name"]} |{car["color"]}\n')

        print(round(sys.getsizeof(cars_arr), 1), "bytes")
        print(round(time.perf_counter() - time_start, 3), "s elapsed time")


    start2()
