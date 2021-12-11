import csv

users = []
hobby = []

with open('users.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    for line in reader:
        users.append(' '.join(line))

# print(users)

with open('hobby.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    for line in reader:
        hobby.append(' '.join(line))

# print(hobby)

users_hobby = dict((users[i], hobby[i]) if len(hobby) > i else (users[i], None) for i in range(len(users)))

# with open('users_hobby_h.txt', 'w', encoding='utf-8') as f:
#     for line in range(len(users_hobby)):
#         f.write(str(users_hobby.items()))
    # f.write(f'{users_hobby}\n')

print(users_hobby)
