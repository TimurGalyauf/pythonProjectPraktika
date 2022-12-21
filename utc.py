import requests
import json
from config import keys
class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')
        try:
            quote_label = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')
        try:
            base_label = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту{base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        valuta_dict_all = json.loads(response.content)['Valute']
        for object in valuta_dict_all:
            if quote == 'рубль':
                quote_value = 1
            else:
                quote_value = valuta_dict_all[quote_label]['Value']
            if base == 'рубль':
                base_value = 1
            else:
                base_value = valuta_dict_all[base_label]['Value']
        response = float(amount) * quote_value / base_value
        return response