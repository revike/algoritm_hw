"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

from time import time


def check_time():
    return time()


def list_data():
    data = []
    start = check_time()
    for i in range(1, 10000000):
        data.append(i)
    end = check_time()
    return end - start


def dict_data():
    data = {}
    start = check_time()
    for i in range(1, 10000000):
        data[i] = i
    end = check_time()
    return end - start


if dict_data() < list_data():
    print(f'Словарь заполняется быстрее на {(list_data() - dict_data()):.{3}f}')
else:
    print(f'Список заполняется быстрее на {(dict_data() - list_data()):.{2}f}')
