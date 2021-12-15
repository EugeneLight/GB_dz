import os
import django


def dir_stat(n=7):
    """
    :param n: задаёт количество ключей в получаемом словаре, по умолчанию 7
    :return: словарь, в котором ключи — верхняя граница размера файла, а значения — общее количество файлов
    """
    folder = django.__path__[0]
    levels = [pow(10, i) for i in range(1, n)]
    files_stat = dict.fromkeys(levels, 0)
    for root, dirs, files in os.walk(folder):
        for file in files:
            size = os.stat(os.path.join(root, file)).st_size
            for idx, val in enumerate(levels):
                if 0 <= size < levels[idx]:
                    files_stat[val] += 1
                    break
                if levels[idx - 1] <= size < levels[idx]:
                    files_stat[val] += 1
                    break
    for key, value in files_stat.items():
        print(f'{key}: {value}')


dir_stat()
