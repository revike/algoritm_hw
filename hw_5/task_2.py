"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""


from collections import deque


def number_input():
    numbers = '0123456789ABCDIF'
    a = input('Введите первое шестнадцатиричное число: ')
    a_list = deque(list(a.upper()))
    for i in a_list:
        if i in numbers:
            pass
        else:
            print('\nТакого шестнадцатиричного числа не существует!\n')
            return number_input()
    b = input('Введите второе шестнадцатиричное число: ')
    b_list = deque(list(b.upper()))
    for j in b_list:
        if j in numbers:
            pass
        else:
            print('\nТакого шестнадцатиричного числа не существует!\n')
            return number_input()
    return result(a_list, b_list)


def result(a_list, b_list):
    res_a = []
    res_c = []
    addition = (hex(int(''.join(a_list), 16) + int(''.join(b_list), 16))).split('x')[-1]
    composition = (hex(int(''.join(a_list), 16) * int(''.join(b_list), 16))).split('x')[-1]
    res_addition = deque(list(addition.upper()))
    res_composition = deque(list(composition.upper()))
    for a in res_addition:
        res_a.append(a)
    for b in res_composition:
        res_c.append(b)
    print(f'\nСумма: {res_a}\nПроизведение: {res_c}')


number_input()
