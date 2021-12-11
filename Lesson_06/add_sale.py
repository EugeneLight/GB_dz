from sys import argv

name, sale = argv


def add_sale(sale):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{float(sale)}\n')
    print(f'Added {sale}')


add_sale(sale)
