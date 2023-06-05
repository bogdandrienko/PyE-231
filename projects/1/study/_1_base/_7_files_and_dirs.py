########################################################################################################################
# TODO работа с текстовыми файлами

import json
import os
import shutil

# open('имя_и_расширение_файла', 'режим_открытия')
# режимы: w r a wb rb w+ r+

# ручное закрытие файла
file1 = open('z_new.txt', mode='w')  # файловый-объект, если файл в папке 'data' - open('data/z_new.txt', 'w')
file1.write("Python is awesome!123\n\thi")
# print(1/0)
file1.close()

file1 = open('z_new.txt', mode='w')  # файловый-объект, если файл в папке 'data' - open('data/z_new.txt', 'w')
try:
    file1.write("Python is awesome!123\n\thi")
except Exception as error:
    print(error)
else:
    pass
finally:
    file1.close()

# контекстный менеджер
with open('z_new.txt', 'r') as file2:
    line1 = file2.read()
    print(line1)

    lines1 = file2.readlines()
    print(lines1)
    # внутри контекстного менеджера

# снаружи контекстного менеджера

# class New_open:
#     def __init__(self, file_name, mode):
#         self.file = open(file_name, mode)
#
#     def __enter__(self):
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#
# with New_open('z_new.txt', 'r') as f:
#     line1 = f.read()


########################################################################################################################

########################################################################################################################
# TODO работа с JSON - файлами

# Serialize obj as a JSON formatted (де-факто стандарт для веба)
# сериализация obj (Python) => JSON
# де сериализация JSON => obj (Python)

dict1 = {"name": "Bogdan"}
# запись
with open('data/new.json', 'w') as file1:
    # todo сразу запись словаря в файл
    json.dump(dict1, file1)

    # todo сначала сериализуем словарь в json_строку
    # str1_json = json.dumps(dict1)
    # file1.write(str1_json)

dict_str1 = json.dumps(dict1)
print(dict_str1)

# JSON в виде строки (часто приходит из "интернет" запросов)
dict_str2 = """[
        {"IIN": '14124152452', "age": 24, "Name": "Bogdan1", "married": false},
        {"IIN": '14124152453', "age": 24, "Name": "Bogdan2", "married": false},
        {"IIN": '14124152454', "age": 24, "Name": "Bogdan3", "married": true},
        {"IIN": '14124152455', "age": 24, "Name": "Bogdan4", "married": false},
        {"IIN": '14124152456', "age": 24, "Name": "Bogdan5", "married": false},
    ]"""
# dict2 = json.loads(dict_str2)

# чтение
# with open('data/new.json', 'r') as file2:
#     # todo сразу чтение словаря из файла
#     dict3 = json.load(file2)
#     print(dict3)

# todo сначала сериализуем json_строку в словарь
# dict4 = json.loads(file2.read())
# print(dict4, type(dict4))

print("\n\n\n\n\n\n***********\n\n\n\n\n\n")
########################################################################################################################

########################################################################################################################
# TODO работа с папками

print(os.getcwd())
# first = os.path.abspath(os.path.dirname(__file__))    # c//github/...  содержит абсолютный путь к текущему скрипту
first = '.'  # // содержит относительный путь к текущему скрипту

second = "temp\\junk2.txt"  # \ - изоляция символа   \n - перенос строки, \t - табуляция...
third = r"temp\junk2.txt"  # \ - изоляция символа   \n - перенос строки, \t - табуляция...
fourth = "temp/junk2.txt"  # \ - изоляция символа   \n - перенос строки, \t - табуляция...

path = os.path.join(second, third)  # temp\junk2.txt + \ + temp\junk2.txt
print(f"path: {path}")

# os.remove("temp/junk.json")
# os.remove("../junk.json")
# try:
#     os.remove("junk.json")  # удаление файла
# except Exception as error:
#     print(error)

try:
    # os.rmdir('temp')  # удаление пустой папки
    shutil.rmtree('temp')  # удаление не пустой папки
except Exception as error:
    print(error)

try:
    os.mkdir("data1")  # make directory
except Exception as error:
    print(error)

# for filename in os.listdir('C:\\Windows'):
#     print(filename)

for filename in os.listdir('.'):
    try:
        print(filename.split(".")[-1])
        # print(filename[::-1].find('.'))  # get index first of char
    except Exception as error:
        pass


# os.rename()  # переименовать
# os.path.exists()

# shutil.copy()
# shutil.move()

def get_all_files_in_path(p=os.path.dirname(os.path.abspath('__file__'))):
    files_list = []
    for root, dirs, files in os.walk(p, topdown=True):
        for name in files:
            files_list.append(f"{os.path.join(root, name)}")
    return files_list


print(get_all_files_in_path())


def get_all_dirs_in_path(p=os.path.dirname(os.path.abspath('__file__'))):
    directories_list = []
    for root, dirs, files in os.walk(p, topdown=True):
        for name in dirs:
            directories_list.append(f"{os.path.join(root, name)}")
    return directories_list


print(get_all_dirs_in_path())


def create_folder_in_this_dir(folder_name='new_folder', current_path=os.path.dirname(os.path.abspath('__file__'))):
    full_path = current_path + f'/{folder_name}'
    try:
        os.makedirs(full_path)
    except Exception as err:
        print(f'directory already yet | {err}')
    finally:
        return full_path


create_folder_in_this_dir("temp2")

# В папке выше текущей(если нет папки, создать)
# дописать в текстовый файл(если нет файла, создать)
# надпись 'Python is awesome'

current_path = "."  # relative - относительный
top_path = "../temp"  # relative - относительный
txt = 'Python is awesome'
if not os.path.exists(top_path):
    os.mkdir(top_path)
with open(f"{top_path}/temp.txt", mode="a", encoding="utf-8") as file:
    file.write(txt + "\n")

print("\n\n\n\n\n\n***********\n\n\n\n\n\n")
########################################################################################################################

########################################################################################################################
# TODO импорт функций и библиотек

from utils import get_square2
# from ..utils import get_square

# импорт всей библиотеки
import time
import random
import tkinter
import datetime

from random import randint

# импорт всех функций, классов и переменных из библиотеки ! Может вызвать коллизию имён !


from math import *  # ALL!

# импорт всей библиотеки с присовением псевдонима(кличка) / alias
import tkinter as tk
from tkinter import ttk
from datetime import date as dt



print(sqrt(16.0), "ЧУЖОЙ")


def sqrt(x):
    return int(x ** 0.5)


print(sqrt(16.0), "НАШ")

print(get_square2(4))
# print(get_square(4))

print(random.randint(1, 1000))
print(randint(1, 1000))
