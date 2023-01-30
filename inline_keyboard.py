from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint

bot_tooken= "6102315312:AAH8QSZL-afysmAEORAx8V2RcieRedIz520"
bot_username='@Amin201516_bot'

bot = Bot(token=bot_tooken)
dp = Dispatcher(bot)

button1 = InlineKeyboardButton(text="btn1", callback_data="btn1")
button2 = InlineKeyboardButton(text="btn2", callback_data="btn2")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2)

button3 = InlineKeyboardButton(text="btn3", callback_data="btn3")
button4 = InlineKeyboardButton(text="btn4", callback_data="btn4")
keyboard_inline2 = InlineKeyboardMarkup().add(button3, button4)

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello! Im Gunther Bot, Please follow my YT channel", reply_markup=keyboard_inline)


@dp.callback_query_handler(text=["btn1", "btn2"])
async def random_value(call: types.CallbackQuery):
    if call.data == "btn1":
        await call.message.answer(randint(1, 10))
    elif call.data == "btn2":
        await call.message.answer('x',reply_markup=keyboard_inline2)
    
    await call.answer()


@dp.callback_query_handler(text=["btn3", "btn4"])
async def random_value(call: types.CallbackQuery):
    if call.data == "btn3":
        await call.message.answer(randint(11, 20))
    elif call.data == "btn4":
        await call.message.answer(randint(11, 20))
    
    await call.answer()

executor.start_polling(dp)