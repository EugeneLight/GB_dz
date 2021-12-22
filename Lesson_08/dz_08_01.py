import re


def email_parse(mail):
    text = re.compile(r"(\w+)@(\w+\.\w+)")
    if text.match(mail):
        print({'username': text.match(mail)[0].split('@')[0], 'domain': text.match(mail)[0].split('@')[1]})
    else:
        raise ValueError(f'wrong email: {mail}')


try:
    email_parse('someone@geekbrains.ru')
except ValueError as e:
    print(e)
