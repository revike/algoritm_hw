"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

import cProfile
from timeit import Timer


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return int(revers_num)


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def main():
    enter_num = 1234567890123456789
    revers(enter_num)
    revers_2(enter_num)
    revers_3(enter_num)


cProfile.run('main()')

print(revers(123456789))
t_r = Timer("revers", "from __main__ import revers")
print('revers ', t_r.timeit(number=10000), 'milliseconds')

print(revers_2(123456789))
t_r_2 = Timer("revers_2", "from __main__ import revers_2")
print('revers_2 ', t_r_2.timeit(number=10000), 'milliseconds')

print(revers_3(123456789))
t_r_3 = Timer("revers_3", "from __main__ import revers_3")
print('revers_3 ', t_r_3.timeit(number=10000), 'milliseconds')


"""
Чаще revers_2 самый эффективный и быстрый!
"""
