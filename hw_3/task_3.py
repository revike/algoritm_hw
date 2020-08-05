"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""


from hashlib import sha256


def substrings(string):
    result = set()
    i = 0
    while i <= len(string):
        str_hash_1 = sha256(string[0:i].encode()).hexdigest()
        str_hash_2 = sha256(string[i:len(string)].encode()).hexdigest()
        result.add(str_hash_1)
        result.add(str_hash_2)
        i += 1
    print(f'\nResult: {len(result) - 1}')


string = input('Введите строку: ')
substrings(string)
