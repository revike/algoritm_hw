"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


from random import randint


def riddle_game(list_numb=[]):
    list_numbs = list_numb
    number = randint(0, 100)
    list_numbs.append(number)
    user_number = int(input('Угадайте число: '))
    if len(list_numbs) == 10 and list_numbs[0] != user_number:
        print(f':( Было загаданно число {list_numbs[0]}')
    elif list_numbs[0] == user_number:
        print(f'Ура! Вы угадали! Число {list_numbs[0]}')
    elif user_number > list_numbs[0]:
        print(f'Слишком большое число!\n'
              f'Осталось попыток - {10 - len(list_numbs)}\n')
        riddle_game(list_numbs)
    elif user_number < list_numbs[0]:
        print(f'Слишком маленькое число!\n'
              f'Осталось попыток - {10 - len(list_numbs)}\n')
        return riddle_game(list_numbs)


riddle_game()
