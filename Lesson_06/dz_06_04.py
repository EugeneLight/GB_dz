import csv

users = []
hobby = []

with open('users.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    for line in reader:
        users.append(' '.join(line))

with open('hobby.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    for line in reader:
        hobby.append(' '.join(line))

users_hobby = (f'{users[i]}: {hobby[i]}\n' if len(hobby) > i else f'{users[i]}: None\n' for i in range(len(users)))

with open('users_hobby.txt', 'w', encoding='utf-8') as f:
    for i in range(len(users)):
        f.write(next(users_hobby))
