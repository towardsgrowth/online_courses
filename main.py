from data.loader import bot, db
import users



if __name__ == '__main__':
    db.delete_info()
    db.create_table_courses()
    bot.infinity_polling()