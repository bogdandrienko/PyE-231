########################################################################################################################
# TODO исключения (try-except)

# операции: транзакции, арифметические (деление на ноль), работа с папками (которых не существует) ...
# print(1/0)  # division by zero
# print("" * "")
# умножение строки на строку
# чтение файла или папки, которых нет
# dict1 = {"name": "Bogdan"}
# print(dict1["name1"])
# KeyError - ключа нет в словаре

# print("Снятие денег с нашего счёта")
# chet = {"ФИО1": "14134525rt214"}
# num = chet["ФИО"]  # взятие из словаря ключа которого нет
# print("na" * "10")  # умножение не тех типов данных
# print(1 / round(0.000000001, 3))  # division by zero
# print("Пополняется счёт друга")


try:
    print("Снятие денег с нашего счёта")

    # print(1 / 0)
    print("na" * "10")

    print("Пополняется счёт друга")

except ZeroDivisionError as error:  # ошибка деления на 0
    print(error)
    print("Возврат средства на мой счёт")
except Exception as error:
    print(error)
    print("Возврат средства на мой счёт (особенная ошибка)")

# все виды: https://www.tutorialspoint.com/object_oriented_python/images/custom_exception_class.jpg

try:
    print("Сняли деньги с моего счёта")
    print("опасные операции 1")
    print(1 / 0)
    print("опасные операции 2")
    print("Перевели деньги на счёт друга")
except ZeroDivisionError as error:  # todo ошибка деления на 0
    print(error)
    print("Перевели деньги назад на мой счёт")
except Exception as error:  # todo ОБЩАЯ ОШИБКА
    print("Перевели деньги назад на мой счёт")
    print(error)
# except:  # todo DANGER
#     pass
else:  # todo УСПЕШНО (ни одной ошибки)
    print("Перевод денег успешно завершён!")
finally:  # todo ВСЕГДА
    # открыли файл - закрыть файл
    # открыли соединение с базой данных - закрыли соединение
    print("Уведомление пользователя о статусе перевода (успешный / не успешный)")


# вызов исключения
try:
    def div2(a, b):
        if b == 0:
            raise Exception  # вызов исключения
        result = a / b
        if result <= 0:
            raise ArithmeticError  # вызов исключения
        return result

    print(div2(1, 0))
except Exception as error:
    print("ERROR")
    print(error)


########################################################################################################################

########################################################################################################################
# TODO собственный класс исключений (try-except)

class MyException(Exception):
    def __init__(self, message: str):
        self.message = message

    def get_error_message(self) -> str:
        return f"состояние: {self.message}"

    def __str__(self) -> str:
        return self.get_error_message()


try:
    print("открытие соединения с базой")

    print("опасные операции 1")
    print(1 / 0)
    print("опасные операции 2")
except MyException as error:
    print(f"Наш код упал! {error.get_error_message()}")
except Exception as error:
    print(f"неизвестная ошибка в операциях!")
    print(error)
else:
    print("ошибки не было!")
finally:
    print("Закрытие соединения с базой")

########################################################################################################################
