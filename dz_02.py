number = 0
num_sum = 0
result_1 = 0
result_2 = 0
i = 0
cube_list = []

while number < 1000:
    if number % 2 != 0:                 # если число нечётное
        cube_num = number ** 3          # возводим его в куб
        cube_list.append(cube_num)      # и добавляем в массив
    number += 1                         # крутим барабан
print(cube_list)                        # выводим список
for n in cube_list:
    num_sum = 0                         # сбрасываем сумму
    while n >= 10:
        num_sum += n % 10               # добавляем в сумму последнюю цифру
        n = n // 10                     # уменьшаем N на цифру
    num_sum += n                        # добавляем в сумму остаток
    if num_sum % 7 == 0:                # если сумма цифр кратна 7
        result_1 += cube_list[i]        # добавляем число в итоговую сумму
    i += 1
print(result_1)                         # выводим итоговую сумму
i = 0
for i, k in enumerate(cube_list):       # перебираем список
    cube_list[i] += 17                  # увеличиваем каждое значение на 17
print(cube_list)
i = 0
for n in cube_list:
    num_sum = 0
    while n >= 10:
        num_sum += n % 10
        n = n // 10
    num_sum += n
    if num_sum % 7 == 0:
        result_2 += cube_list[i]
    i += 1
print(result_2)