def thesaurus_adv(*args):
    surnames_dict = {}
    for idx in sorted(list(args)):
        surnames_dict.setdefault(idx.split()[1][:1], {}).setdefault(idx.split()[0][:1], []).append(idx)
    return surnames_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
