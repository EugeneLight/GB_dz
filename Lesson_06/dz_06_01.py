data_list = []

with open('nginx_logs.txt', encoding='utf-8') as f:
    result = ((line.split()[0], line.split()[5].strip('"'), line.split()[6]) for line in f)
    for idx in result:
        data_list.append(idx)
print(data_list)

with open('data_from_nginx.txt', 'w', encoding='utf-8') as f:
    for line in data_list:
        f.write(str(f'{line}\n'))
