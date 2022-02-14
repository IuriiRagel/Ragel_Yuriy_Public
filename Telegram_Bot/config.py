import requests
import json

TOKEN = "5157667962:AAH1u0n987ynrDSD5z_2PvdA-HWbE0_UC2I"
# создаем словарь только с обычными валютами (USD, EUR). Криптовалюты будут в него дописываться из API запроса
keys = {'dollar':'USD', 'euro':'EUR'}

# задаем количество криптовалют, которые будут добавлены в словарь (топ-N)
N_currencies = 10

# API-запрос на топ N валют по объему в USD за последние 24 часа
top_list = requests.get(f'https://min-api.cryptocompare.com/data/top/totalvolfull?limit={N_currencies}&tsym=USD')

# содержимое запроса парсим в json и из полученного словаря данные по ключу Data сохраняем в переменную
currencies = json.loads(top_list.content)['Data']

# переменная currencies -- это список словарей словарей из N элементов
# Элемент currency[i] -- это словарь для i-ой валюты, где по ключу 'CoinInfo' вложен словарь
# в котором есть данные о коде валюты (ключ 'Name') и ее полном названии ('FullName')
# перебираем словарь currencies по этим ключам, и записываем в словарь,
# при условии, если такого ключа еще нет в словаре а
# обратите внимание, что для FullName используется метод lower(), так как в общении с ботом используются названия валют
# только строчными буквами

for i in range(len(currencies)):
    currency_code = currencies[i]['CoinInfo']['Name']
    currency_name = currencies[i]['CoinInfo']['FullName'].lower().replace(' ','_')
    if currency_name not in keys.keys():
        keys[currency_name] = currency_code

# здесь мы отправляем API запрос на получение списка всех криптовалют (около 7000)
# это даст возможность искать валюту не только среди ограниченного набора keys
# но и среди всех доступных на сайте (благодаря этому пользователь сможет сделать запрос например
# monacoin dollar 30 и получить ответ
url='https://min-api.cryptocompare.com/data/all/coinlist'
all_coins = json.loads(requests.get(url).content)['Data']
name = 'bitcoin'
full_key = {}

for key in all_coins:
    full_key[all_coins[key]['CoinName'].replace(' ', '_').lower()]=key