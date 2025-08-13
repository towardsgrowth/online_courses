from telebot.types import Message, BotCommand
from data.loader import bot, db
from keyboards.dafault import make_default_buttons, yes_or_no
from config import main_default_buttons




bot.set_my_commands(commands=[
    BotCommand("start", "botni ishga tushurish")


])

@bot.message_handler(commands=['start'])
def reaction_to_start(message:Message):
    chat_id = message.chat.id
    full_name =message.from_user.full_name
    bot.send_message(chat_id, f"Assalamu alaykum {full_name}!!!\n"
                              f"Bizning botimizdan foydalanayotganingizdan xursandmiz!!!\n\n"
                              f"Quyidagilardan foydalanishingiz mumkin👇:", reply_markup=make_default_buttons(main_default_buttons))

# ----------------------------------------------------------------------------------------------------------------------------------------------->
@bot.message_handler(func=lambda message: message.text == "Ma'lumot qo'shish➕")
def reaction_to_malumot_qoshish(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "Kurs nomini kiriting: ")
    bot.register_next_step_handler(msg, save_course)


def save_course(message: Message):
    chat_id = message.chat.id
    course_name = message.text
    db.add_course(course_name)
    bot.send_message(chat_id, "Muvafaqqiyatli qo'shildi!!!\n\nYana kurs qo'shmoqchimisiz👇:", reply_markup=yes_or_no())
@bot.message_handler(func=lambda message: message.text == "Ha👌")
def reaction_to_yes(message:Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "Kurs nomini kiriting: ")
    bot.register_next_step_handler(msg, reaction_to_yes_only)

def reaction_to_yes_only(message:Message):
    chat_id = message.chat.id
    course_name = message.text
    db.add_course(course_name)
    bot.send_message(chat_id, "Muvafaqqiyatli qo'shildi!!!\n\nYana kurs qo'shmoqchimisiz👇:", reply_markup=yes_or_no())

@bot.message_handler(func=lambda message: message.text == "Yo'q🚫")
def reaction_to_no(message:Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Siz quyidagi sahifadasiz👇 :", reply_markup=yes_or_no())

@bot.message_handler(func=lambda message: message.text == "Orqaga🔙")
def reaction_to_no(message:Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Asosiy menu👇 :", reply_markup=make_default_buttons(main_default_buttons))
# ---------------------------------------------------------------------------------------------->



