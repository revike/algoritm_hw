"""
Задание 7.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""


class QueueClass:
    def __init__(self):
        self.queue_base = []
        self.queue = []
        self.solved = []

    def is_empty_base(self):
        """очередь базовая"""
        return self.queue_base == []

    def is_empty(self):
        """очередь на доработку"""
        return self.queue == []

    def is_empty_solved(self):
        """решено"""
        return self.solved

    def to_queue_base(self, item):
        """добавление в базовую очередь"""
        self.queue_base.append(item)

    def to_queue(self, item):
        """добавление в очередь на доработку"""
        self.queue.append(item)

    def to_solved(self, item):
        """добавление в решенные"""
        self.solved.append(item)

    def from_queue_base(self):
        """извлечение из базовой очереди"""
        return self.queue_base.pop()

    def from_queue(self):
        """извлечение из очереди на доработку"""
        return self.queue.pop()

    def from_solved(self):
        """Извлечение решеных задач"""
        return self.solved.pop()


if __name__ == '__main__':
    sc_obj = QueueClass()


def queue(tasks):
    obj = QueueClass()
    queue_base = ''
    queue = ''
    solved = ''
    for k, v in tasks.items():
        if v == -1:
            obj.to_queue_base(k)
            queue_base += obj.from_queue_base() + ' '
        elif v == 0:
            obj.to_queue(k)
            queue += obj.from_queue() + ' '
        else:
            obj.to_solved(k)
            solved += obj.from_solved() + ' '

    print('Задачи:', queue_base)
    print('Задачи на доработку:', queue)
    print('Решено:', solved)


# -1 -> нерешенные
# 0  -> на доработку
# 1  -> решенные

tasks = {
    'Задача1': -1,
    'Задача2': 0,
    'Задача3': 1,
    'Задача4': -1,
    'Задача5': 0,
    'Задача6': 1,
    'Задача7': -1,
    'Задача8': 0,
    'Задача9': 1,
    'Задача10': -1,
    'Задача11': 0,
    'Задача12': 1,
}


queue(tasks)
