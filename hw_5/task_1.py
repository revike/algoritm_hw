"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""

from collections import namedtuple, Counter, OrderedDict, defaultdict


def score_company():
    try:
        n = input('Введите количество предприятий: ')
        if int(n) < 0:
            return score_company()
        return companies(int(n))
    except ValueError:
        print('\nНеобходимо ввести количество предприятий!\n')
        return score_company()
    except ZeroDivisionError:
        print('Тогда Пока!')


def companies(n, result=[]):
    if n == 0:
        return answer(result)
    else:
        try:
            res = namedtuple('company', 'name quarter_1 quarter_2 \
                                quarter_3 quarter_4')
            comp = input('Введите название компании: ')
            profit = input('Введите прибыль за кварталы через пробел: \n')
            resume = res(
                name=comp,
                quarter_1=int(profit.split()[0]),
                quarter_2=int(profit.split()[1]),
                quarter_3=int(profit.split()[2]),
                quarter_4=int(profit.split()[3])
            )
            mean = (resume.quarter_1 + resume.quarter_2 + resume.quarter_3 + resume.quarter_4) / 4
            result.append((resume.name, mean))
            return companies(n - 1, result)
        except IndexError:
            print('\nВы допустили ошибку! Начнем сначала!\n')
            return score_company()


def answer(result):
    mean_profits = 0  # Средняя годовая прибыль всех предприятий
    i = 0
    while i < len(result):
        mean_profits += result[i][-1]
        i += 1
    mean_profit = mean_profits / i
    mean_company = f'Средняя годовая прибыль всех предприятий: {mean_profit}'

    res_up = []
    res_down = []

    while i > 0:
        if result[i-1][-1] > mean_profit:
            res_up.append(result[i-1][0])
        elif result[i - 1][-1] < mean_profit:
            res_down.append(result[i-1][0])
        i -= 1

    print(f'\n{mean_company}')
    if res_up:
        print('Предприятия, с прибылью выше среднего значения:', ', '.join(res_up))
    if res_down:
        print(f'Предприятия, с прибылью ниже среднего значения:', ', '.join(res_down))
    if not res_down and not res_up:
        print('Средняя прибыль все предприятий равна средней прибыли каждого предприятия!')


score_company()
