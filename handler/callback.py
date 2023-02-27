from aiogram import types, Dispatcher
from config import bot, db

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

def reg_hand_callback(db:Dispatcher):
    db.register_callback_query_handler(quiz2, text='button')