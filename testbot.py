import sqlite3
import asyncio
import logging
from aiogram import Dispatcher, types, executor
from token_bot import bot
#from aiogram.fsm.context import FSMContext

logging.basicConfig(level=logging.INFO)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
	await bot.send_message(message.chat.id,"bot work!")
	keyboard=types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
	create_user=types.KeyboardButton(text='Создать пользователя')
	keyboard.add(create_user)
	await bot.send_message(message.chat.id,"Для того чтобы создать воспользуйтесь клавиатурой ниже", reply_markup=keyboard)


@dp.message_handler(text=['Создать пользователя'])
async def create_user(message:types.Message):
	await bot.send_message(message.from_user.id, f"Вы {message.from_user.full_name}?")
	
	#await bot.send_message(message.chat.id,"Введите имя, фамилию")

   # await state.set_state(NameChoosing.choosing_name_lastname)
	
	
    

async def main():
	await dp.start_polling(bot)

if __name__=="__main__":
	asyncio.run(main())

