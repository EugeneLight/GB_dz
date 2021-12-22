from os import path, getcwd, walk
from shutil import copytree


def templates():
    full_path = path.join(getcwd(), 'my_project')
    for root, dirs, files in walk(full_path):
        for file in files:
            to_path = path.join(path.join(full_path, 'templates'), path.relpath(root, full_path).split('\\')[0])
            if file.rsplit('.')[-1].lower() == 'html' and not path.exists(to_path):
                copytree(root, to_path)


templates()
