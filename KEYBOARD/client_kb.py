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
start_markup.add(start_button, quiz_button, location, contact, reg_button)

cancel = KeyboardButton('cancel')

submit_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('yes'),
                                                                  KeyboardButton('Lets do it again'),
                                                                  cancel
                                                                                      )


gender_markup=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                                                                  KeyboardButton('Male'),
                                                                  KeyboardButton('Female'),
                                                                  KeyboardButton('Other'),
                                                                  cancel
                                                                                    )
cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(cancel)