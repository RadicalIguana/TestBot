import sqlite3
import asyncio
import logging
from aiogram import Dispatcher, types, executor
from token_bot import bot
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
#from aiogram.fsm.context import FSMContext

logging.basicConfig(level=logging.INFO)
memstore=MemoryStorage()
dp=Dispatcher(bot, storage=memstore)

class Form(StatesGroup):
	first_name=State()
	last_name=State()
	phone_name=State()

@dp.message_handler(text=['Создать пользователя'], state=None)
async def asd(message: types.Message):
	await bot.send_message(message.chat.id, "Введите ваше имя")
	await Form.first_name.set()
	
@dp.message_handler(state=Form.first_name)
async def set_fname(message: types.Message, state:FSMContext):
	async with state.proxy() as proxy:
		proxy['first_name']= message.text
		await Form.last_name.set()
	await bot.send_message(message.chat.id, "Введите вашу фамилию")

@dp.message_handler(state=Form.last_name)
async def set_lname(message:types.Message, state:FSMContext):
	async with state.proxy() as proxy:
		proxy['last_name']=message.text
		await Form.phone_name.set()
	await bot.send_message(message.chat.id,"Введите ваш номер телефона")
	
@dp.message_handler(state=Form.phone_name)
async def phone_name(message:types.Message, state:FSMContext):
	async with state.proxy() as proxy:
		proxy['phone_name']=message.text
		await state.finish()
	s=await state.get_data()
	await bot.send_message(message.chat.id,"Пользователь успешно создан!\n"f'Ваши данные: {s.get("first_name")} {s.get("last_name")} {s.get("phone_name")}')

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
	await bot.send_message(message.chat.id,"bot work!")
	keyboard=types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
	create_user=types.KeyboardButton(text='Создать пользователя')
	keyboard.add(create_user)
	await bot.send_message(message.chat.id,"Для того чтобы создать воспользуйтесь клавиатурой ниже", reply_markup=keyboard)


@dp.message_handler(text=['Создать пользователя'])
async def create_user(message:types.Message):
	#await bot.send_message(message.from_user.id, f"Вы {message.from_user.full_name}?")
	await bot.send_message(message.chat.id,"Введите имя")
	
   # await state.set_state(NameChoosing.choosing_name_lastname)


	
    

async def main():
	await dp.start_polling(bot)

if __name__=="__main__":
	asyncio.run(main())

