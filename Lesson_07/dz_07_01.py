from os import path, mkdir
from yaml import load
from yaml.loader import BaseLoader


def starter():
    with open('preform.yaml') as f:
        dirs_dict = load(f, Loader=BaseLoader)
    md_list = tuple(dirs_dict.keys())
    for d in md_list:
        if not path.exists(d):
            mkdir(d)
    print(*md_list, sep=', ')
    dd_list = tuple(*dirs_dict.values())
    for d in dd_list:
        sub_dir = path.join(md_list[0], d)
        if not path.exists(sub_dir):
            mkdir(sub_dir)
    print(*dd_list, sep=', ')


starter()