"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
from timeit import Timer


_list = range(1, 100)


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(func_1(_list))
t1 = Timer("func_1", "from __main__ import func_1")
print('func_1 ', t1.timeit(number=1000000), 'milliseconds')

# ___________________________________


def func_2(nums, i=0, new_arr=None):
    if new_arr is None:
        new_arr = []
    try:
        if nums[i] % 2 == 1:
            return func_2(nums, i + 1, new_arr)
        elif nums[i] % 2 == 0:
            new_arr.append(i)
            return func_2(nums, i + 1, new_arr)
    except IndexError:
        return new_arr


print(func_2(_list))
t2 = Timer("func_2", "from __main__ import func_2")
print('func_2 ', t1.timeit(number=10000), 'milliseconds')


"""
Сделал функцию func_2, которая добавляет в новый список индексы с помощью рекурсии
Работает быстрее

Пробовал через генератор! Получалось 50/50
new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
"""
