def odd_nums(n):
    for num in range(1, n + 1, 2):
        yield num


for odd_num in odd_nums(int(input('Введите число: '))):
    print(odd_num)
