from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from KEYBOARD.client_kb import *
class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    gender = State()
    region = State()
    photo = State()
    submit = State()

async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.name.set()
        await message.answer('Kak vas zovut?',reply_markup=cancel_markup)

async def fsm_name(message: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date['id'] = message.from_user.id
        date['username'] = message.from_user.username
        date['name'] = message.text
        print(date)
    await FSMAdmin.next()
    await message.answer('What is your age?', reply_markup=cancel_markup)
async def fsm_age(message: types.Message, state: FSMContext):
    async with state.proxy() as date:
        if 17 <= int(message.text) <= 99:
            date['age'] = message.text
            await FSMAdmin.next()
            print(date)
            await message.answer('What is your gender?', reply_markup=gender_markup)
        else:
            await message.answer('Oh!')

async def fsm_gender(message:types.Message, state:FSMContext):
    async with state.proxy() as date:
        date['gender'] = str(message.text)
        await FSMAdmin.next()
        print(date)
    await message.answer('Where are you from?', reply_markup=cancel_markup)

async def fsm_region(message:types.Message, state:FSMContext):
    async with state.proxy() as date:
        date['region'] = str(message.text)
        await FSMAdmin.next()
        print(date)
        await message.answer('Cool! I like it')
        await message.answer('Send a photo', reply_markup=cancel_markup)

async def fsm_photo(message: types.Message, state: FSMContext):
    print(message)
    async with state.proxy() as date:
        date['photo'] = message.photo[0].file_id

        await message.answer_photo(date['photo'], caption=f'{date["name"]} {date["age"]}'
                                        f'{date["gender"]} @{date["username"]}')
    await FSMAdmin.next()
    await message.answer("OK?", reply_markup=submit_markup)

async def submit(message:types.Message, state:FSMContext):
    if message.text.lower() == 'YEs':
        await message.answer('you are under my cover')
        await state.finish()
    elif message.text == 'lets do it again':
        await message.answer('What is your name?')
        await message.answer('sdf')


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("You are not under my cover anymore")
        await message.answer('/start')
def reg_hand_anketa(db: Dispatcher):
    db.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True), state='*')
    db.register_message_handler(fsm_start, commands=['reg'])
    db.register_message_handler(fsm_name, state=FSMAdmin.name)
    db.register_message_handler(fsm_age, state=FSMAdmin.age)
    db.register_message_handler(fsm_gender, state=FSMAdmin.gender)
    db.register_message_handler(fsm_region, state=FSMAdmin.region)
    db.register_message_handler(fsm_photo, state=FSMAdmin.photo, content_types=['photo'])
    db.register_message_handler(submit, state=FSMAdmin.submit)