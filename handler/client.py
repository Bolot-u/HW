from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, db
from KEYBOARD.client_kb import start_markup
async def start_handler(message: types.Message):
        await bot.send_message(message.from_user.id, f'hello {message.from_user.first_name}',
                                reply_markup=start_markup)
        await message.answer('пока что все')
        #await message.reply(message.from_user.first_name)


@db.message_handler(commands=['quiz'])
async def quiz1(message:types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next',callback_data='button')
    markup.add(button)
    ques = 'Откуда мем?'
    answer = [
        'Ввостание планеты шимпанзе',
        'Ввостание планеты человеков',
        'Ввостание планеты обезьян',
        'Ввостание машин'
    ]
    photo = open('media/868589bca82aca20132ad176d3b45b40.jpg', 'rb')
    await bot.send_photo(message.from_user.id,photo=photo)
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        reply_markup=markup
    )

def reg_client(db:Dispatcher):
    db.register_message_handler(start_handler,commands=['hello', 'start'])
    db.register_message_handler(quiz1,commands=['quiz'])
