sec_input = int(input('Введите количество секунд: '))

sec_balance = sec_input % 60
minutes = sec_input // 60
hours = minutes // 60
days = hours // 24
minutes = minutes - (hours * 60)
hours = hours - (days * 24)

print(days, 'дн', hours, 'час', minutes, 'мин', sec_balance, 'сек')