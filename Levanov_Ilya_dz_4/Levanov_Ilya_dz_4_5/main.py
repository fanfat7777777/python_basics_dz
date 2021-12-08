from requests import get, utils
import sys
import time
import datetime
from decimal import Decimal

def currency_rates(char_code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    currency_dict = {}
    for n in content.split('</Value>'):  # Находим код валюты и её значения
        i = n.split('</CharCode>')[0][-3:]
        currency_dict[i] = n[-7:] if i.isalpha() else print()  # Создаём список с валютой и её стоимостью

    d_serv = time.strptime(response.headers['Date'], "%a, %d %b %Y %H:%M:%S %Z")
    days = datetime.date(d_serv.tm_year, d_serv.tm_mon, d_serv.tm_wday)     #Получаем дату
    char_code = char_code.upper()               #Приводим к одному регистру для простоты сравнения
    if currency_dict.setdefault(char_code) == None:
        print('Неверный код валюты')
    else:                                       #Если ключ есть в списке выдаём значение валюты
        price = Decimal(currency_dict[char_code].replace(',', '.')).quantize(Decimal('0.01'))
        print(f'{char_code} = {price}, {days}')
        print(type(price), type(days))

#В терминале: python main.py USD или др код валюты
currency_rates(sys.argv[1]) if __name__ == '__main__' and len(sys.argv) > 1 else currency_rates('usd')