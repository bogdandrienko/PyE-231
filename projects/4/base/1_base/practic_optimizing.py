import random
import sys
import time


def bad():
    start = time.perf_counter()

    car_names = ["Toyota", "Honda", "Audi", "Nissan"]
    car_colors = ["Black", "Blue", "Red", "Yellow", "White"]
    car_count = 50000000  # 50000000

    def get_data():
        cars = []
        for i in range(1, car_count + 1):
            new_car = {
                "id": i,
                "name": random.choice(car_names),
                "color": random.choice(car_colors)
            }
            cars.append(new_car)
        return cars

    all_cars = get_data()
    print(type(all_cars), all_cars)  # list

    print(round(sys.getsizeof(all_cars) / 1024 / 1024, 1), "megabytes")  # 5000000 = 41.9 megabytes

    with open("bad.txt", "w", encoding="utf-8") as file:
        for car in all_cars:
            file.write(f'{car["id"]} | {car["name"]} |{car["color"]}\n')

    stop = time.perf_counter()

    print(round((stop - start), 2))  # 6.94

def good():
    start = time.perf_counter()

    car_names = ["Toyota", "Honda", "Audi", "Nissan"]
    car_colors = ["Black", "Blue", "Red", "Yellow", "White"]
    car_count = 50000000  # 50000000

    def get_data():
        for i in range(1, car_count + 1):
            new_car = {
                "id": i,
                "name": random.choice(car_names),
                "color": random.choice(car_colors)
            }
            yield new_car

    all_cars = get_data()
    print(type(all_cars), all_cars)  # <class 'generator'> <generator object good.<locals>.get_data at 0x000002AA87199840>

    print(round(sys.getsizeof(all_cars) / 1024 / 1024, 1), "megabytes")  # 5000000 = 41.9 megabytes

    with open("bad.txt", "w", encoding="utf-8") as file:
        for car in all_cars:
            file.write(f'{car["id"]} | {car["name"]} |{car["color"]}\n')

    stop = time.perf_counter()

    print(round((stop - start), 2))  # 6.96

# bad()
good()
