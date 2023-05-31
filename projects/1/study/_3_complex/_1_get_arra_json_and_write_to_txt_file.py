import json

# 1 прочитать json
# todo открытие json-файла на чтение с помощь контекстного менеджера
with open("temp/data2.json", mode='r', encoding="utf-8") as json_file:
    # todo конвертация json-файла в "питоновский" словарь (list[dict])
    dictionaries = json.load(json_file)

    # print(dictionaries)
    # print(type(dictionaries))       # <class 'list'>
    # print(type(dictionaries[0]))    # <class 'dict'>

# 2 записать txt
# todo открытие txt-файла на запись с помощь контекстного менеджера
with open("temp/data2.txt", mode='w', encoding="utf-8") as txt_file:
    # todo перебор всех словарей и запись данных из каждого на новую строку в txt-file
    for dictionary in dictionaries:
        #     10 | 199 | ipsam aperiam voluptates qui | 1
        user_id = dictionary['userId']
        _id = dictionary['id']
        title = dictionary['title']
        completed = dictionary['completed']

        new_string = f"{user_id} | {_id} | {title} | {completed}\n"
        txt_file.write(new_string)

# todo COMPACT
# with open("temp/data2.json", mode='r', encoding="utf-8") as json_file:
#     with open("temp/data2.txt", mode='w', encoding="utf-8") as txt_file:
#         for dictionary in json.load(json_file):
#             txt_file.write(f"{dictionary['userId']} | {dictionary['id']} | {dictionary['title']} | {dictionary['completed']}\n")
