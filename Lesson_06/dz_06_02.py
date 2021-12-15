from collections import Counter

with open('data_from_nginx.txt', encoding='utf-8') as data:
    line = data.read().split("'")
    ip_list = [idx for idx in line if idx.replace('.', '').isdigit()]

print(f'Спаммер - {Counter(ip_list).most_common(1)[0][0]}')
print(f'Количество запросов - {Counter(ip_list).most_common(1)[0][1]}')
