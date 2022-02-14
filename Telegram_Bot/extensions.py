import requests
import json
from config import keys, full_key

# cоздание класса исключений как ребенка класса Exception
class APIException(Exception):
    pass

# cоздание класса КриптоКонвертера для получения данных по API запросу и просчета цены на заданное количество валюты
# метод get_price сначала пытается найти валюту в коротком словаре keys,
# и если не находит, переходит к полному словарю full_keys
class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        
        if quote == base:
            raise APIException("Исходная и конечная валюты должны быть разными")

        try:
            base_ticker = keys[base]
        except:
            try:
                base_ticker = full_key[base]
                keys[base] = base_ticker
            except KeyError:
                raise APIException(f"Не удалось конвертировать валюту {base}")

        try:
            quote_ticker = keys[quote]
        except:
            try:
                quote_ticker = full_key[quote]
                keys[quote] = quote_ticker
            except KeyError:
                raise APIException(f"Не удалось конвертировать валюту {quote}")



        try:
            amount = float(amount)
        except ValueError:
            raise APIException("Не удалось обработать количество")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]*amount
        return total_base

