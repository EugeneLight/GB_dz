import os

with open('preform.csv', encoding='utf-8') as dirs:
    start_dir, start_pack_l2 = dirs.read().split('\n')
    start_pack_l2 = tuple(start_pack_l2.split(', '))

if not os.path.exists(start_dir):
    os.mkdir(start_dir)
os.chdir(start_dir)
for idx in range(len(start_pack_l2)):
    if not os.path.exists(start_pack_l2[idx]):
        os.mkdir(start_pack_l2[idx])
