from telebot.types import Message, BotCommand, ReplyKeyboardMarkup, KeyboardButton
from config import main_default_buttons


def make_default_buttons(l:list):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for i in main_default_buttons:
        markup.add(i)
    return markup

def yes_or_no():
    markup =ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = KeyboardButton("Ha👌")
    btn2 = KeyboardButton("Yo'q🚫")
    markup.add(btn2,btn1)
    btn3 = KeyboardButton("Orqaga🔙")
    markup.add(btn3)
    return markup

def cancel():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton("Bekor qilish")
    markup.add(btn)
    return markup

