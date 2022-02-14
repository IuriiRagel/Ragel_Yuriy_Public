This Python script uses pyTelegramBotAPI package for Telegram Bot @money_rates_bot (Currency_Exchange)

The Telegram bot connects to API https://min-api.cryptocompare.com/ to retrieve cryptocurrency rates
User can ask Telegram bot what currency he want to get, in which currency to price it, and the amount
The bot then will use this input to retrieve the latest rates and calculates the total.

config.py -- contains Telegram Bot token and dictionary with currencies and their codes for API request
extensions.py -- contains two classes used in the script: APIException(Exception) and CryptoConverter to convert the currency
Telegram_bot_object.py -- main script to launch the Telebot

Please make sure to put all scripts in same folder to launch the bot.

We also added a fun function '/hint' which suggests to try out a new crypto out of more than 7000+ list.
Please note that some of the crypto currencies from that list don't have a trading history, so there won't be an exchange rate
for examples https://min-api.cryptocompare.com/data/price?fsym=HIBS&tsyms=USD
would return an error "cccagg_or_exchange market does not exist for this coin pair (HIBS-USD)"
