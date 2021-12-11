def thesaurus(*args):
    names_dict = {}
    for idx in sorted(list(args)):
        names_dict.setdefault(idx[:1], []).append(idx)
    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
