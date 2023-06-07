########################################################################################################################
# TODO регулярные выражения

import re

input_from_user1 = "qwerty"  # Q werty # 1 111111
input_from_user1.isascii()  # пароль должен быть на английском
input_from_user1.islower()  # только маленькие ли?
input_from_user1.isdigit()  # только цифры?
input_from_user1.isalpha()

# минимум 12 знаков, максимум 16, маленькая и большая буква, спецсимвол и цифра

# 00000000 - 99999999 | мгновенно
# 00000000 - Zzzzzzzz | мгновенно
# https://thesecurityfactory.be/password-cracking-speed/

txt = r"   (?=^.{8,}$)  ((?=.*\d)   |  (?=.*\W+))   (?![.\n])   (?=.*[A-Z])  (?=.*[a-z])  .*$"

pattern2 = r'^   (?=.*[a-z])  (?=.*[A-Z]) (?=.*\d)  (?=.*[0-9])   [A-Za-z\d]   {12,16}   $'
txt2 = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{12,}$"
# внутри круглых скобок - это требование
# внутри квадратных скобок - это разрешение на ввод
# внутри фигурных скобок - требуемая длина

# todo password check
password1 = "111111111"
password2 = "123456789qwerty!"
password3 = "123456789Qwerty!"

cond1 = re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{12,}$",
                 string=password3)
if cond1 is None:
    print("Пароль не подходит")
else:
    print("Пароль подходит")
print(cond1, type(cond1))
# re.search()


while False:  # True
    a1 = input("Введите новый пароль:  ").strip()  # python
    print(a1)
    if not re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{12,}$",
                    string=a1):
        print("\n\nОшибка ввода, повторите ввод!\n")
        continue
    b1 = input("Введите новый пароль ещё раз:  ").strip()  # python
    if a1 != b1:
        print("\n\nПароли не совпадают!\n")
        continue

    print("Пароль успешно применён", a1)
    break


def validate_email(mail: str) -> bool:
    # @gmail.com
    # admin@com
    # admin@gmail.com
    if re.match(r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,}$", string=mail) is not None:
        return True
    # else
    return False


print(validate_email("@gmail.com"))
print(validate_email("admin@com"))
print(validate_email("admin@gmail.com"))
print(validate_email("admin1234@gmail.com"))
print(validate_email("admin1234@gmail.CLINIC"))
print(validate_email("admin1234@gmail.KANIKULI"))
# False
# False
# True
# True
# Fals
# e
# phone check
#                         8-777-635-76-86
phoneRegex1 = re.compile(r"\d-\d\d\d-\d\d\d-\d\d-\d\d")

#                         777-635-76-86
phoneRegex2 = re.compile(r"\d\d\d-\d\d\d-\d\d-\d\d")
# (\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})

# https://python.ivan-shamaev.ru/python-3-regular-expressions-regex-match-group-string/
