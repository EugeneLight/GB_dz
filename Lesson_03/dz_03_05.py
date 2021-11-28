# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
# случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный",
# "мягкий"]
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы
# слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы
# сделать аргументы именованными?

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом", "кот", "хлеб", "фотоаппарат"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "почти уже"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "родной", "пушистый"]


def get_jokes(n=5, repeat=None, idx=0):
    """
    Укажите количество шуток, которое требуется вывести\n
    Также укажите, разрешается ли использовать слова повторно
    """
    jokes_list = []
    min_len = min(len(nouns), len(adverbs), len(adjectives))
    while idx < n:
        if repeat == 'да' or repeat == 'yes':
            jokes_list.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}'.capitalize())
        else:
            if n <= min_len:
                jokes_list.append(f'{nouns.pop(random.randrange(0, len(nouns)))} {adverbs.pop(random.randrange(0, len(adverbs)))} {adjectives.pop(random.randrange(0, len(adjectives)))}'.capitalize())
            else:
                print(f'Не, не, давай не больше {min_len}!')
                return
        idx += 1
    print(', '.join(jokes_list))


get_jokes(int(input('Введите кол-во шуток: ')), input('Повторы разрешать? '))
