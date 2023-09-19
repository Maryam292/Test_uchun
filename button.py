from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
registr1 = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton("Ro`yxatdan O`tish!")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
send_contact = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton('Send Contact', request_contact = True)
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)