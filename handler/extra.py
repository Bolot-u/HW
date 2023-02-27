from aiogram import types, Dispatcher
from config import bot, db
import random
async def echo(message: types.Message):
    emoji_list = ['\U0001F600','\U0001F601','\U0001F602','\U0001F607','\U0001F608']
    if message.text == 'python':
        await bot.send_message(message.chat.id, random.choice(emoji_list))


def reg_hand_extra(db:Dispatcher):
    db.register_message_handler(echo)