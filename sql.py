from aiogram import Dispatcher, Bot, executor, types
import logging
import sqlite3

##############################################################################
#---------------------------------MySQL Config-------------------------------#                                                                        
##############################################################################



link = sqlite3.connect('bd.db')

cursor = link.cursor()


#######################################
#--------------Config Bot-------------#
#######################################

logging.basicConfig(level=logging.INFO)
bot = Bot(token="6574070168:AAH4IRznQ44WOcwiDH34DMy-6uFjvttW5Mg")
dp = Dispatcher(bot=bot)


#########################################
#------------------Start----------------#
#########################################

# @dp.message_handler(content_types=['text'])
# async def text(message):

#     if message.chat.type == 'private':
@dp.message_handler(content_types=types.ContentType.ANY)
async def echo_message(message: types.Message):
        user_id = message.from_user.id
        name = message.from_user.first_name
        username = message.from_user.username
        contact = message.contact

        # try:
        ##### SQL поиск#####
        query = f"INSERT INTO users (`name`, `username`, `nomer`, `user_id`) VALUES ( '{name}', '{username}', '{contact}', '{user_id}');"        #,(user_id, name, contact,)
        cursor.execute(query)
        link.commit()
        #####################
        # except:
        #     ############SQL замена и запис результата#############
        #     query = f"UPDATE users SET name = {name}, username = {username}, nomer = {contact} WHERE user_id = {user_id};"
        #     cursor.execute(query)
        #     link.commit()
        #     ######################################################



#################################################
#------------------Начало роботы----------------#
#################################################
try:
    if __name__ == "__main__":
        print("Казино Бот запущен проблем нет")
        executor.start_polling(dp, skip_updates=True)
except Exception as _ex:
    print("Ошыбка!!!!!!!!!\n", _ex)
