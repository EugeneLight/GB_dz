# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором
# ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее
# количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
# но больше предыдущей (начинаем с 0).

import os
from os.path import relpath
from collections import  defaultdict

import django

# folder = django.__path__[0]
# files_stat = defaultdict(list)
# for root, dirs, files in walk(folder):
#     for file in files:
#         ext = file.rsplit('.', maxsplit=1)[-1].lower()
#         rel_path = relpath(path.join(root, file), folder)
#         files_stat[ext].append(rel_path)
# print(files_stat)

folder = django.__path__[0]
levels = [0, 10, 100, 1000]
files_stat = dict.fromkeys(levels, 0)
for root, dirs, files in os.walk(folder):
    # print(root)
    # print(dirs)
    # print(files)
    # print()
    for file in files:
        for idx in range(len(levels)):
            if levels[idx - 1] * 2 ** 10 < os.stat(os.path.join(root, file)).st_size < levels[idx] * 2 ** 10:
                files_stat[levels[idx]] += 1
print(files_stat)

# levels = [0, 10, 100, 1000]
# files_stat = dict.fromkeys(levels, 0)
# for file in scandir(folder):
#     for idx in range(len(levels)):
#         if (levels[idx - 1] * 2 ** 10 < file.stat().st_size < levels[idx] * 2 ** 10):
#             files_stat[levels[idx]] += 1
# print(files_stat)
