"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""

from timeit import Timer


def recursive_reverse(number):
    if number == 0:
        return str(number)  # в третьем варианте сделала эту строку 'return str(number)[:-1]' чтобы убрать лишний ноль
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


print(recursive_reverse(123456789))

t1 = Timer("recursive_reverse", "from __main__ import recursive_reverse")
print('recursive_reverse ', t1.timeit(number=10000), 'milliseconds')

# _______ВАРИАНТ_2______________


def recursive_rev(number):
    res = ''
    while number != 0:
        res += str(number % 10)
        number = number // 10
    return int(res)


print(recursive_rev(123456789))

t2 = Timer("recursive_rev", "from __main__ import recursive_rev")
print('recursive_rev ', t2.timeit(number=10000), 'milliseconds')


# _____ВАРИАНТ_3___МЕМОИЗАЦИЯ


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


@memoize
def rec_rev(number):
    if number == 0:
        return str(number % 10)[:-1]
    return f'{str(number % 10)}{rec_rev(number // 10)}'


print(rec_rev(123456789))

t3 = Timer("rec_rev", "from __main__ import rec_rev")
print('rec_rev ', t3.timeit(number=10000), 'milliseconds')

"""
В вашем коде вконце появляется '0' нечаянно
Сделал вариант 2 без мемоизации и у брал рекурсию. Написал цикл while
В 3 варианте как по заданию с мемоизацией и ваш код...
"""
