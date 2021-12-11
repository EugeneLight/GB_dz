def num_translate_adv(word):
    num_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if word.istitle():
        return num_dict.get(word.lower()).title()
    else:
        return(num_dict.get(word))


print(num_translate_adv(input('Введите число: ')))
