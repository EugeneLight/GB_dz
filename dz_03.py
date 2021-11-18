number = 1

while number < 101:
    str_number = str(number)
    figure = list(str_number)
    if int(figure[-1]) == 1 and (number < 10 or number > 15):
        print(str_number, 'процент')
    elif 1 < int(figure[-1]) < 5 and (number < 10 or number > 15):
        print(str_number, 'процента')
    else:
        print(str_number, 'процентов')
    number += 1
