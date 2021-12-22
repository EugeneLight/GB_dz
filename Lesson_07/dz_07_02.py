from yaml import load
from yaml.loader import BaseLoader
from os import path, mkdir

with open('config.yaml') as f:
    dirs_dict = load(f, Loader=BaseLoader)

md_list = tuple(dirs_dict.keys())
for d in md_list:
    if not path.exists(d):
        mkdir(d)
print(*md_list, sep=', ')
sub_dir_list = tuple(*dirs_dict.values())
print(*sub_dir_list, sep=', ')
dd_list2 = dict(*dirs_dict.values())
for d in sub_dir_list:
    sub_dir = path.join(md_list[0], d)
    if not path.exists(sub_dir):
        mkdir(sub_dir)
content = dd_list2[sub_dir_list[0]]
for file in content:
    my_file = open(path.join(md_list[0], sub_dir_list[0], file), 'w')
print(content)
# for idx in range(len(sub_dir_list)):
    # print(dd_list2[sub_dir_list[idx]])
    # content = tuple(dd_list2[sub_dir_list[idx]])
    # print(content)
    # for file in content:
    #     my_file = open(file, 'w')
    # break
# dd_list3 = list(*dd_list2.values())
# print(dd_list3)

print()
