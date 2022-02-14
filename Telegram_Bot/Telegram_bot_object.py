import telebot, requests, json
# библиотеки requests и json нужны для получения топ криптовалют (команда /top)

from config import keys, TOKEN
# словарь keys составляется каждый раз при запуске скрипта бота из API запроса на топ валют
# по умолчанию словарь keys содержит USD, EUR + top-10 криптовалют за последние 24 часа
# для изменения размера словаря достаточно изменить переменную N_currencies в config.py

from extensions import APIException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

# обработчик команды start
@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = 'Приветствую! Этот бот конвертирует крипто/валюты. ' \
           '\nЧтобы начать работу, введите команду боту в следующем формате:\
     \n<имя валюты> <в какую валюту перевести> <количество переводимой валюты> \
     \nНапример: bitcoin dollar 50 ' \
           '\n\n Список команд бота:' \
           '\n /start -- инструкция использования бота' \
           '\n /values -- список доступных валют' \
           '\n /top -- Топ-10 криптовалют за 24 часа' \
           '\n /help -- помощь'
    bot.reply_to(message,text)

# обработчик команды help
@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = 'Для конвертации введите две валюты через пробел и количество валюты, например:' \
           '\nbitcoin dollar 10' \
           '\nЕсли количество валюты не введено, то будет выведена стоимость 1 единицы' \
           ''
    bot.reply_to(message,text)

# обработчик команды values
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:\n"
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

# обработчик команды top -- бот посылает API запрос на топ-10 валют за последние 24 часа
# производит парсинг в json и достает оттуда названия криптовалют
@bot.message_handler(commands=['top'])
def top(message: telebot.types.Message):
    text = "Топ-10 крипто за последние 24 часа:\n"
    r_top = requests.get('https://min-api.cryptocompare.com/data/top/totalvolfull?limit=10&tsym=USD')
    r_list = json.loads(r_top.content)['Data']
    for i in range(len(r_list)):
        text = '\n'.join((text, r_list[i]['CoinInfo']['FullName']))
    bot.reply_to(message, text)

#обработка команды по конвертации валют с некоторыми модификациями
@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    # так как автокоррекция многих телефонов может исправлять начало ввода на заглавную букву,
    # то мы используем метод .lower() для приведения к строчным буквам
    # использование метода .split() без параметров позволяет разбивать ввод
    # по любому количеству пробелов или разрывов строк
    values = message.text.lower().split()
    try:
        # допускаем случай, если валюты введены верно, но не введено количество
        # в таком случае принимаем количество валюты = 1 и пытаемся обработать ввод
        if len(values) == 2:
            values.append(1)

        if len(values) != 3:
            raise APIException("Простите, я не смог распознать команду.\nВведите две валюты через пробел и количество. Например:"
                               "\nbitcoin dollar 10"
                               "\nвведите /values для получения списка валют")

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message,f"Неверный ввод\n{e}")
    except Exception as e:
        bot.reply_to(message,f"Не удалось обработать команду\n{e}")
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)



bot.polling(none_stop=True)