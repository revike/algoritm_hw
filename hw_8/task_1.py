"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""

from collections import deque, defaultdict


def haff_tree(strings):
    count = defaultdict(int)
    for string in strings:
        count[string] += 1
    count_sort = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(count_sort) != 1:
        while len(count_sort) > 1:
            w = count_sort[0][1] + count_sort[1][1]
            c = {0: count_sort.popleft()[0],
                    1: count_sort.popleft()[0]}

            for i, cnt in enumerate(count_sort):
                if w > cnt[1]:
                    continue
                else:
                    count_sort.insert(i, (c, w))
                    break
            else:
                count_sort.append((c, w))
    else:
        w = count_sort[0][1]
        c = {0: count_sort.popleft()[0], 1: None}
        count_sort.append((c, w))
    return count_sort[0][0]


table = dict()


def haff_code(tree, path=''):
    if not isinstance(tree, dict):
        table[tree] = path
    else:
        haff_code(tree[0], path=f'{path}0')
        haff_code(tree[1], path=f'{path}1')


s = "Hello world!"
haff_code(haff_tree(s))


for i in s:
    print(table[i], end=' ')
