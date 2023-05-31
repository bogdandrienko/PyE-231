import json

# txt
# txt_file = open("temp/data.txt", mode="r", encoding="utf-8")  # r w a rb wb
# try:
#     print(txt_file.readlines()[10])  #
# except Exception as error:
#     print(error)
# finally:
#     print("закрытие файла")
#     txt_file.close()

# todo TXT-файл
with open("temp/data.txt", mode="r", encoding="utf-8") as file:
    # todo Контекстный менеджер "with" обязательно закрывает файл в любых случаях(включая исключения)
    print(file.readlines())

# todo JSON-файл
# чтение
with open("temp/new.json", mode="r", encoding="utf-8") as file:
    data = json.load(file)
    # load - десериализация (JSON -> Python Dict)
    print(data)
    print(type(data))

# запись
with open("temp/data.json", mode="w", encoding="utf-8") as file:
    dict1 = {"Mansur": 4.8, "Meiram": 4.9}
    print(type(dict1))

    json.dump(dict1, file)
    # dump - сериализация (Python Dict -> JSON)


