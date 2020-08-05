"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""

from uuid import uuid4
from hashlib import sha256


def password_true():
    password = input('Введите пароль: ')
    salt = uuid4().hex
    psw_result = sha256(password.encode() + salt.encode()).hexdigest()
    print(psw_result)
    password_2 = input('Введите пароль повторно: ')
    psw_result_2 = sha256(password_2.encode() + salt.encode()).hexdigest()
    print(psw_result_2)
    if psw_result == psw_result_2:
        return True
    else:
        return False


print('\n', password_true())
