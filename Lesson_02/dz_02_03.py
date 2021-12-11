start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for idx, word in enumerate(start_list):
    if word.replace('+','').isdigit():   # проверяем, цифра ли
        if int(word.find('+')) == 0:     # если перед цифрой +
            word = word.strip('+')       # отрубаем его нахер
            word = f'+0{word}'
        elif int(word) < 10:
            word = f'0{word}'
        start_list[idx] = f'"{word}"'
print(' '.join(start_list))