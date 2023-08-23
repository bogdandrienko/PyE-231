# Пишем программу для бухгалтерии, с интерфейсом(внешний вид)
# это windows 10, 1.exe и внутри папки есть некоторое количество json файлов
# по нажатию на кнопку "старт" программа должна "складывать" все эти файлы в один итоговый
# уникальность по id
# https://jsonplaceholder.typicode.com/todos
import json
import os
import tkinter as tk


def example():
    def start():
        data = []
        for root, dirs, files in os.walk("temp", topdown=True):
            for name in files:
                extension = name.split(".")[-1]
                if extension.lower() == "json":
                    with open(f'temp/{name}', 'r') as file2:
                        data_new = json.load(file2)
                        if isinstance(data_new, list):
                            data.extend(data_new)  # [1, 2, 3] -> [4, 5, 6] = [1, 2, 3, 4, 5, 6]
                        else:
                            data.append(data_new)  # [1, 2, 3] -> [4, 5, 6] = [1, 2, 3, [4, 5, 6]]
        new_data = []
        print("\n\n\nOLD: ")
        for d in data:
            print(d)
        for d in data:  # старая коробка
            is_new = True
            for n in new_data:  # новая коробка
                if d["id"] == n["id"]:
                    is_new = False
                    break
            if is_new:
                new_data.append(d)
            else:
                print("эта игрушка уже есть")
        print("\n\n\nnew_data: ")
        for d in new_data:
            print(d)
        with open(f'temp/all.json', 'w') as file3:
            json.dump(new_data, file3)

    root = tk.Tk()
    root.title("Интеллектуальная Бухгалтерия 2.0")
    label = tk.Label(root, text="Положите файлы в папку 'temp' и нажмите 'старт'")
    label.pack(pady=10)
    button = tk.Button(root, text="старт", command=start)
    button.pack()
    root.mainloop()


# чтение (из файлов)
# чистка данных
# соединение
# проверка на уникальность


with open(f'temp/new1.txt', 'r') as file:
    data1 = file.readlines()
    print(type(data1), data1)

    new_data1 = []
    for i in data1:
        clear_data = int(i.strip())  # удаляет все спецсимволы(\n \t ' ')
        new_data1.append(clear_data)
    print(type(new_data1), new_data1)


with open(f'temp/new3.txt', 'r') as file:
    data2 = file.readlines()
    print(type(data2), data2)

    new_data2 = []
    for i in data2:
        clear_data = int(i.strip())  # удаляет все спецсимволы(\n \t ' ')
        new_data2.append(clear_data)
    print(type(new_data2), new_data2)

new_data1.extend(new_data2)
# data = new_data1 + new_data2
data = new_data1

print(type(data), data)
print(type(set(data)), set(data))



















