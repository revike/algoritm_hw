"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def bunch(n, first_num=1, second_num=2, result=[], ress=0):
    res_list = result
    res = n * (n + 1) / 2
    if n == 1 and res_list[0] == ress:
        return True
    else:
        result = first_num + second_num
        res_list.append(res)
        return bunch(n - 1, result, second_num + 1, res_list, result)


print(bunch(3))
