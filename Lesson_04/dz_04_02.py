from requests import get, utils

response = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))


def currency_rates(val):
    content_list = response.split('<Valute ID=')
    for idx in content_list:
        if val.upper() in idx:
            return float(idx[-24:-17].replace(',', '.'))
    else:
        return 'None'


print(currency_rates('eur'))
print(currency_rates('usd'))