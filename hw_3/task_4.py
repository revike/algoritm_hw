"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

from uuid import uuid4
from hashlib import sha256


def url_hash(salt, url_data=[]):
    url = input('"q" - Exit!\nВведите url: ')
    result = sha256(url.encode() + salt.encode()).hexdigest()
    if url == 'q':
        print('Exit')
    elif result in url_data:
        print('Хэш уже существует')
        url_hash(salt)
    else:
        url_data.append(result)
        print('Хэш добавлен!')
        return url_hash(salt)


salt = uuid4().hex
url_hash(salt)
