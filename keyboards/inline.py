from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.loader import bot, db

def make_inline_buttons(k: list):
    markup = InlineKeyboardMarkup()
    for i in k:
        markup.add(InlineKeyboardButton(i, callback_data=i,))
    return markup

