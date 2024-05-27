from aiogram import types

admin_button = [
    [types.KeyboardButton(text="Reklama yuborish 📢"), types.KeyboardButton(text="Admin Qo'shish 🧑‍")],
    [types.KeyboardButton(text="Adminlarga xabar yuborish ✉️💻"), types.KeyboardButton(text="Userlar soni 👤")]
]
admin = types.ReplyKeyboardMarkup(keyboard=admin_button, resize_keyboard=True)
