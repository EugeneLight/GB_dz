import os
from time import perf_counter

folder = 'some_data'
start = perf_counter()
all_files = [item for item in os.listdir(folder)]
print(len(all_files), perf_counter() - start)

start = perf_counter()
all_files_2 = [item.name for item in os.scandir(folder)]
print(len(all_files_2), perf_counter() - start)
print(all_files == all_files_2)
