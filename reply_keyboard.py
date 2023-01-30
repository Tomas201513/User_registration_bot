# https://www.youtube.com/watch?v=HXVi2zT7l_c

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from random import randint

bot_tooken= "6102315312:AAH8QSZL-afysmAEORAx8V2RcieRedIz520"
bot_username='@Amin201516_bot'

bot = Bot(token=bot_tooken)
dp = Dispatcher(bot)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("Hi", "Ola",'info')  #list z buttons horizontally 

#or
# keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("Hi").add("Ola")  #list z buttons vertically

#or
# button1=KeyboardButton('Hi')
# button2=KeyboardButton('Ola')
# keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2)


# keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("contact", "location") 

button3=KeyboardButton('contact',request_contact=True)
button4=KeyboardButton('location',request_location=True)
keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button3).add(button4)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello! Im Gunther Bot, Please follow my YT channel", reply_markup=keyboard1)



# @dp.message_handler(commands=['info'])
# async def welcome(message: types.Message):
#     await message.reply("share us smtg!", reply_markup=keyboard2)


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == 'Hi':
        await message.reply("Hi! How are you?")
    elif message.text == 'Ola':
        await message.reply("https://youtube.com/gunthersuper")
    elif message.text == 'info':
        await message.reply("share us smtng!",reply_markup=keyboard2)
    else:
        await message.reply(f"Your message is: {message.text}")



executor.start_polling(dp)