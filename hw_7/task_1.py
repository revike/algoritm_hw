"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort(orig_list))
print(timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=1))

print('______________')

orig_list = [random.randint(-100, 100) for _ in range(100)]
print(orig_list)
print(bubble_sort(orig_list))
print(timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=1))

print('______________')

orig_list = [random.randint(-100, 100) for _ in range(1000)]
print(orig_list)
print(bubble_sort(orig_list))
print(timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=1))

print('______________')
print('______________')
print('______________')


def bubble_sort(lst_obj):
    """Если за проход по списку не совершается ни одной сортировки, то завершение"""
    n = 1
    k = 1
    while n < len(lst_obj):
        if k >= len(lst_obj):
            break
        else:
            for i in range(len(lst_obj) - n):
                if lst_obj[i] < lst_obj[i + 1]:
                    lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                    k = 1
                if lst_obj[i] > lst_obj[i + 1]:
                    k += 1
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort(orig_list))
print(timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=1))

print('______________')

orig_list = [random.randint(-100, 100) for _ in range(100)]
print(orig_list)
print(bubble_sort(orig_list))
print(timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=1))

print('______________')

orig_list = [random.randint(-100, 100) for _ in range(1000)]
print(orig_list)
print(bubble_sort(orig_list))
print(timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=1))


"""
При сортировке 10 элементов:
До оптимизации:
1.2200000000000405e-05
После оптимизации:
7.200000000012752e-06

print(1.2200000000000405e-05 > 7.200000000012752e-06) -> True
=======================

При сортировке 100 элементов:
До оптимизации:
0.0005803999999999983
После оптимизации:
5.209999999999937e-05

print(0.0005803999999999983 > 5.209999999999937e-05) -> True
=======================

При сортировке 1000 элементов:
До оптимизации:
0.06403139999999999
После оптимизации:
0.0016045000000000087

=======================

Из результатов видно что после оптимизации
сортировка происходит в разы быстрее!
"""
