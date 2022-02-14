import requests
import json
from config import keys

# cоздание класса исключений как ребенка класса Exception
class APIException(Exception):
    pass

# cоздание класса КриптоКонвертера для получения данных по API запросу и просчета цены на заданное количество валюты
class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException("Исходная и конечная валюты должны быть разными")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f"Не удалось конвертировать валюту {quote}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f"Не удалось конвертировать валюту {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise APIException("Не удалось обработать количество")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]*amount
        return total_base

