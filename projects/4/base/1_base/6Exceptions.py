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

print("12")
# print(1 / 0)  # падение потока (кода)
print("13")

try:
    print("Сняли деньги с моего счёта")

    print("опасные операции 1", 1 / 0)

    print("Перевели деньги на счёт друга")
except ZeroDivisionError as error:  # ошибка деления на 0
    print(error)
    print("Ошибка конвертации!")
except Exception as error:
    print("Ошибка перевода!")
    print("Перевели деньги назад на мой счёт")
    print(error)
else:
    print("Перевод денег успешно завершён!")
finally:
    print("Уведомление пользователя о статусе перевода (успешный / не успешный)")


# все виды: https://www.tutorialspoint.com/object_oriented_python/images/custom_exception_class.jpg

# вызов исключения
try:
    def div2(a, b):
        if b == 0:
            raise ZeroDivisionError  # вызов исключения
        result = a / b
        if result <= 0:
            raise ArithmeticError  # вызов исключения
        return result
except ZeroDivisionError as error:  # перехват исключения
    print(error)
except Exception as error:  # перехват исключения
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
