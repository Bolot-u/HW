from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
    )
start_button = KeyboardButton("/hello")
quiz_button = KeyboardButton("/quiz")
reg_button = KeyboardButton("/reg")

location = KeyboardButton("location", request_location=True)
contact = KeyboardButton("contact", request_contact=True)
user = KeyboardButton("user", request_user=None)
start_markup.add(start_button, quiz_button, reg_button, location, contact, user)