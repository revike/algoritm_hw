"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
from statistics import median as med
from random import randint


# 1.
def median_1(m):
    arr = []
    i = 1
    while i <= (2 * m + 1):
        arr.append(randint(1, 100))
        i += 1
    return med(arr)


def input_number():
    global number
    try:
        number = int(input('Введите любое натуральное число: '))
        if number < 0:
            print('Нужно ввести положительное число!\n')
            input_number()
    except ValueError:
        input_number()
    return number


m = input_number()
print(f'Первый вариант: {median_1(m)}')


# 2. Без сортировки
def median_2(m):
    arr = []
    i = 1
    while i <= (2 * m + 1):
        arr.append(randint(1, 100))
        i += 1
    k, l, r = 0, 0, 0
    while k < len(arr):
        l, r = 0, 0
        for j in arr:
            if j > arr[k]:
                l += 1
            if j < arr[k]:
                r += 1
        if l == r:
            return arr, arr[k]
        else:
            k += 1


print(f'Второй вариант: {median_2(m)}')
