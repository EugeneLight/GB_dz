from json import dump
from itertools import zip_longest

users = []
hobby = []

with open('users.csv', encoding='utf-8') as f:
    for line in f.read().split('\n'):
        users.append(line.replace(',', ' '))

with open('hobby.csv', encoding='utf-8') as f:
    for line in f.read().split('\n'):
        hobby.append(line)

users_hobby = dict(zip_longest(users, hobby, fillvalue=None))

with open('dict_uh.json', 'w', encoding='utf-8') as f:
    dump(users_hobby, f, ensure_ascii=False, indent=4)

print(users_hobby)
