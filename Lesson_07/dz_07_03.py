from os import path, getcwd, walk
from shutil import copytree

full_path = path.join(getcwd(), 'my_project')

for root, dirs, files in walk(full_path):
    for file in files:
        if file.rsplit('.')[-1].lower() == 'html'\
                and not path.exists(path.join(path.join(full_path, 'templates'),
                                              path.relpath(root, full_path).split('\\')[0])):
            copytree(root, path.join(path.join(full_path, 'templates'), path.relpath(root, full_path).split('\\')[0]))
