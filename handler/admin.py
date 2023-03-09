from aiogram import types, Dispatcher
from config import bot, ADMIN
from .extra import users
async def ban(message:types.Message):
    if message.chat.type !='private':
        text = message.text.split()
        name = text[1]
        await bot.kick_chat_member(message.chat.id, user_id = users[f'{name}'])
    else:
        await message.answer('I cant my baby')

def reg_ban(db:Dispatcher):
    db.register_message_handler(ban, commands=['ban'], commands_prefix=['!'])

