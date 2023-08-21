import re


def extra():
    # login == email | number(IIN)
    # password == Aa1##############
    # c = re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")

    password = ""
    while True:
        # best practice:
        # password = input("Введите пароль (минимум 8 знаков, оба регистра, спецсимвол и цифра): ")
        # if re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", string=password):
        #     break

        password = input("Введите пароль (минимум 8 знаков, оба регистра, спецсимвол и цифра): ")
        # print(type(password), password)
        # Qwerty!123
        # qwerty!123

        cond = re.match(
            r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",
            string=password
        )  # <class 're.Match'> | <class 'NoneType'>
        # print(type(cond), cond)  # <class 're.Match'> <re.Match object; span=(0, 10), match='Qwerty!123'>

        if cond is not None:
            print("password is valid")
            break
        print("password is invalid")

    login = ""
    while True:
        # best practice:
        login = input("Введите Ваш логин (минимум 8 знаков, только латинница): ")
        if re.match(r'^[a-z0-9]+[._]?[a-z0-9]+@\w+[.]\w{2,}$', string=login):
            break
        # andrienko.1999@gmail.com #
        # andrienko.19_99@yo.com

    with open("user.txt", "w") as file:
        file.write(f"{login} {password}")


import re


def check(question: str, pattern: str) -> str:
    while True:
        _login = input(question)
        if re.match(pattern, _login):
            return _login
        print("Неверно! Повторите ввод!")


login = check("Введите новый логин: ", r'^[a-z0-9]+[._]?[a-z0-9]+@\w+[.]\w{2,}$')
password = check("Введите новый пароль: ", r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
with open("user.txt", "w") as file:
    file.write(f"{login} {password}")
