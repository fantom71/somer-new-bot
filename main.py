import telebot
from telebot import types

bot = telebot.TeleBot('1690544169:AAHwJeU0mrGyzNuoUBmz2iQ8sc8xXWA4QGQ')

@bot.message_handler(commands=["telegram"])
def telegram(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить telegram", url="https://t.me/Olechkaaa07"))
    bot.send_message(message.chat.id, "Отличный выбор, просто нажмите на кнопку ниже", parse_mode='html', reply_markup=markup)

@ bot.message_handler(commands=["vkontakte"])
def vk(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить Вк", url="https://vk.com/id152150884"))
    bot.send_message(message.chat.id, "Отличный выбор, просто нажмите на кнопку ниже", parse_mode='html', reply_markup=markup)

@ bot.message_handler(commands=["instagram"])
def instagram(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить Инстаграм", url="https://www.instagram.com/olecka06"))
    bot.send_message(message.chat.id, "Отличный выбор, просто нажмите на кнопку ниже", parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.InlineKeyboardButton("/telegram")
    btn2 = types.InlineKeyboardButton("/vkontakte")
    btn3 = types.InlineKeyboardButton("/instagram")
    markup.add(btn1, btn2, btn3)
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nДля связи со мной выберите пункт"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)

