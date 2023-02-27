from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    gender = State()
    region = State()

async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.name.set()
        await message.answer('Kak vas zovut?')

async def load_name(message:types.Message, state:FSMContext):
    async with state.proxy() as date:
        date['id'] = message.from_user.id
        date['username'] = message.from_user.username
        date['name'] = message.text
        print(date)
    await FSMAdmin.next()
    await message.answer('What is your age?')
async def load_age(message:types.Message, state:FSMContext):
    async with state.proxy() as date:
        if 17 <= int(message.text) <= 99:
            date['age'] = message.text
            await FSMAdmin.next()
            print(date)
            await message.answer('What is your gender?')
        else:
            await message.answer('Oh!')

async def load_gender(message:types.Message, state:FSMContext):
    async with state.proxy() as date:
        date['gender'] = str(message.text)
        await FSMAdmin.next()
        print(date)
    await message.answer('Where are you from?')

async def load_region(message:types.Message, state:FSMContext):
    async with state.proxy() as date:
        date['region'] = str(message.text)
        await FSMAdmin.next()
        print(date)
        await message.answer('Cool! I like it')





def reg_hand_anketa(db:Dispatcher):
    db.register_message_handler(fsm_start, commands=['reg'])
    db.register_message_handler(load_name, state=FSMAdmin.name)
    db.register_message_handler(load_age, state=FSMAdmin.age)
    db.register_message_handler(load_gender, state=FSMAdmin.gender)
    db.register_message_handler(load_region, state=FSMAdmin.region)