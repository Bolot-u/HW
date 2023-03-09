from aiogram import types, Dispatcher
from config import bot, db
import random
async def echo(message: types.Message):
    emoji_list = ['\U0001F600','\U0001F601','\U0001F602','\U0001F607','\U0001F608']
    if message.text == 'python':
        await bot.send_message(message.chat.id, random.choice(emoji_list))
    print(message.from_user.id)

users = {}

async def check_ban(message: types.Message):
    username = message.from_user.username
    if username:
        username = username
    else:
        username = message.from_user.first_name
    if message.from_user.username is not users:
        users[f'@{username}'] = message.from_user.id
def reg_hand_extra(db:Dispatcher):
    db.register_message_handler(echo)
    db.register_message_handler(check_ban)