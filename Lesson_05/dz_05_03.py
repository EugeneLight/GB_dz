tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Олег', 'Никита', 'Алина']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

none_gen = {classes.append(None) for n in range(len(tutors)) if len(classes) < len(tutors)}
my_gen = ((surname, classes[idx]) for idx, surname in enumerate(tutors))

print(type(my_gen))
print(*my_gen)
print(tuple(my_gen))

# Сравнивал результаты времени выпонения своего варианта и вашего... Это жесть...
