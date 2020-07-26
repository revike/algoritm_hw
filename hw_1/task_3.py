"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""
from operator import itemgetter

repository_companies = {
    'google': 99989,
    'facebook': 94845,
    'yahoo': 68452,
    'alibaba': 74211,
    'yandex': 84656,
    'tatneft': -4521,
    'gazprom': 0
}


def search_max_profit_1(repository_companies):
    list_profit = []
    result = {}
    for v in repository_companies.values():
        list_profit.append(v)
    profit_3 = sorted(list_profit)[-3:]
    for k, v in repository_companies.items():
        if v in profit_3:
            result[k] = v
    return result
# O(n*2)


def search_max_profit_2(repository_companies):
    result = sorted(repository_companies.items(), key=itemgetter(1))[-3:]
    return result
# O(nlog(n)), но возможно и O(n*2) так как не смог найти что под капотом у модуля
# operator. Тем не менее я б выбрал это решение, т.к. оно компактнее и скорее всего O(nlog(n))


print(search_max_profit_1(repository_companies))
print(search_max_profit_2(repository_companies))
