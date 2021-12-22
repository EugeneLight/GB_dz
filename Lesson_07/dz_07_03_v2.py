import os
from os import path, getcwd
from shutil import copyfile

full_path = path.join(getcwd(), 'my_project')
templates = path.join(full_path, 'templates')

if not path.exists(path.join(templates)):
    os.mkdir(path.join(templates))
    print(f'Folder templates created!')
#
for root, dirs, files in os.walk(full_path):
    for file in files:
        if root != templates:
            if file.rsplit('.')[-1].lower() == 'html' and path.exists(path.join(templates)):
                pre = root.rsplit('\\')[-1]
                copyfile(path.join(root, path.basename(file)),
                                path.join(templates, f'{pre}_{path.basename(file)}'))
print(f'{len(os.listdir(templates))} files copied to {templates}')
