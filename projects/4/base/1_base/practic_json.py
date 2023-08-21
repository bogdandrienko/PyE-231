import json
import os

dict1 = {"name": "Bogdan"}
# запись
with open('data/new.json', 'w') as file1:
    # todo сразу запись словаря в файл
    json.dump(dict1, file1)

print(os.getcwd())

for filename in os.listdir('data'):
    print(filename)

for root, dirs, files in os.walk(".", topdown=True):
    for name in dirs:
        print(root, name)
    for file in files:
        print(root, file)


def get_all_data():
    """Привет Мир!"""
    pass


##############################################

# from tkinter import ttk, Tk, Spinbox  # 20-30 ....
# spin1 = Spinbox()
# tk1 = Tk()

# -: too long import

##############################################

##############################################
# import tkinter as tk
# import tkinter.ttk as ttk
# spin1 = tk.Spinbox()
# tk1 = tk.Tk()

# -: best practice
##############################################

##############################################
# from tkinter import *
# class Spinbox(object):
#     def __init__(self):
#         pass
# spin = Spinbox()
# spin.lower()
