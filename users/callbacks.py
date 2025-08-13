from telebot.types import Message, CallbackQuery
from data.loader import bot, db
from keyboards.inline import make_inline_buttons



@bot.message_handler(func=lambda message: message.text == "Mavjud malumotlar🔍")
def reaction_to_mavjud_malumotlar(message: Message):
    chat_id = message.chat.id
    courses = [row[0] for row in db.get_info()]
    bot.send_message(chat_id, "Quyidagilar mavjud👇:", reply_markup=make_inline_buttons(courses))
# ------------------------------------------------------------------------------------------------------>
@bot.callback_query_handler(func=lambda call: call.data in [row[0] for row in db.get_info()])
def reaction_to_inline_button(call: CallbackQuery):
    inline_button(call)


def inline_button(call: CallbackQuery):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    bot.send_message(chat_id, f"Siz {message_id} tanladingiz!", reply_to_message_id=message_id)




