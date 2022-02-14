This Python script uses pyTelegramBotAPI package for Telegram Bot @money_rates_bot (Currency_Exchange)

The Telegram bot connects to API https://min-api.cryptocompare.com/ to retrieve cryptocurrency rates
User can ask Telegram bot what currency he want to get, in which currency to price it, and the amount
The bot then will use this input to retrieve the latest rates and calculates the total.

config.py -- contains Telegram Bot token and dictionary with currencies and their codes for API request
extensions.py -- contains two classes used in the script: APIException(Exception) and CryptoConverter to convert the currency
Telegram_bot_object.py -- main script to launch the Telebot

Please make sure to put all scripts in same folder to launch the bot.

