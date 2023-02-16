from aiogram import Bot, Dispatcher, types
from decouple import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
TOKEN = config('TOKEN')
bot = Bot(TOKEN)
db = Dispatcher(bot=bot)
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
@db.callback_query_handler(text='button')
async def quiz2(call:types.CallbackQuery):
    ques = 'Откуда этот мем?'
    answer = [
        'Марсианин',
        'Пришелец',
        'Интерстеллер',
        'Интерстеллар',
    ]
    photo = open('media/000844262097a8048f553a5b0dbb083a.jpg', 'rb')
    await bot.send_photo(call.from_user.id,photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
    )