import telebot
from config import keys, TOKEN
from utc import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Что бы начать работу введите комманду боту в следующем формате: \n<имя валюты>\
<в какую валюту перевести>\
<количество переводимой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text ='\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        input_data = message.text.split(' ')
        if len(input_data) != 3:
            raise ConvertionException('Слишком много параметров.')
        quote, base, amount = input_data
        response = CryptoConverter.get_price(quote, base, amount)

    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {keys[quote]} = {round(response, 2)} {keys[base]}'
        bot.send_message(message.chat.id, text)

bot.polling()

