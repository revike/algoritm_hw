"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

from memory_profiler import profile
from numpy import array
from time import time


# 1.
@profile
def func_1():
    res = []
    for i in range(100000):
        res.append(i)
    return res


# 2.
@profile
def func_2():
    res = array([i for i in range(100000)])
    return res


# 3.
def check_time():
    return time()


@profile
def list_data():
    data = []
    start = check_time()
    for i in range(1, 100000):
        data.append(i)
    end = check_time()
    return end - start


# 4.
@profile
def dict_data():
    data = {}
    start = check_time()
    for i in range(1, 100000):
        data[i] = i
    end = check_time()
    return end - start


if __name__ == "__main__":
    func_1()
    func_2()
    list_data()
    dict_data()

"""
1.
Line #    Mem usage    Increment   Line Contents
================================================
    25     22.7 MiB     22.7 MiB   @profile
    26                             def func_1():
    27     22.7 MiB      0.0 MiB   	res = []
    28     24.9 MiB      0.0 MiB   	for i in range(100000):
    29     24.9 MiB      0.2 MiB   		res.append(i)
    30     24.9 MiB      0.0 MiB   	return res

2.
Line #    Mem usage    Increment   Line Contents
================================================
    34     23.3 MiB     23.3 MiB   @profile
    35                             def func_2():
    36     24.7 MiB      0.1 MiB   	res = array([i for i in range(100000)])
    37     24.1 MiB      0.0 MiB   	return res

3.
Line #    Mem usage    Increment   Line Contents
================================================
    45     23.3 MiB     23.3 MiB   @profile
    46                             def list_data():
    47     23.3 MiB      0.0 MiB       data = []
    48     23.3 MiB      0.0 MiB       start = check_time()
    49     24.7 MiB      0.0 MiB       for i in range(1, 100000):
    50     24.7 MiB      0.1 MiB           data.append(i)
    51     24.7 MiB      0.0 MiB       end = check_time()
    52     24.7 MiB      0.0 MiB       return end - start

4.
Line #    Mem usage    Increment   Line Contents
================================================
    56     23.6 MiB     23.6 MiB   @profile
    57                             def dict_data():
    58     23.6 MiB      0.0 MiB       data = {}
    59     23.6 MiB      0.0 MiB       start = check_time()
    60     27.2 MiB      0.0 MiB       for i in range(1, 100000):
    61     27.2 MiB      1.5 MiB           data[i] = i
    62     27.2 MiB      0.0 MiB       end = check_time()
    63     27.2 MiB      0.0 MiB       return end - start


Анализ!
Python 3.7 
OC x64

Первая и вторая функции очень похожи, только во второй функции мы
используем библиотеку numpy, с помощью которой используется меньше памяти.

Третья и четвертая также похожи между собой, только в третье мы добавляем
элементы в список, а в четвертой в словарь. Как мы помним с прошлых уроков,
элементы в словарь добавляется быстрее, а памяти получается используется больше.

"""
