from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')

encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
# print(response.headers['Date'])

currency_dict = {}

for v in content.split('</Value>'):
    i = v.split('</CharCode>')[0][-3:]
    if i.isalpha():
        currency_dict[i] = v[-7:]

def currency_rates(char_code):
    print('Неверный код валюты') if currency_dict.setdefault(char_code) == None \
        else print(f'{char_code} = {currency_dict[char_code]} руб.')

if __name__ == "__main__":
    currency_rates(input('Введите код валюты: '))