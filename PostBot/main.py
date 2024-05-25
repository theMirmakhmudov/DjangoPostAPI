import asyncio
import logging
import os

import requests
from aiogram import Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram import Bot
from aiogram.types import BotCommand
from dotenv import load_dotenv
from aiogram.fsm.context import FSMContext
from states import Register
import cv2

load_dotenv(".env")
TOKEN = os.getenv("TOKEN")
Admin = os.getenv("ADMIN")
Channel = os.getenv("CHANNEL")

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    url = "http://127.0.0.1:8000/"
    response = requests.get(url=url).json()
    user_exist = False
    for i in response:
        if i["user_id"] == message.from_user.id:
            user_exist = True
            break
    if user_exist == False:
        await state.set_state(Register.fullname)
        await message.answer(
            f"<b>Assalomu Aleykum, Xurmatli {message.from_user.mention_html()}\n\nTo'liq FISH kiriting:\nMisol uchun: Ibragimov Musharraf</b>")
    else:
        await message.answer("<b>User already exist</b>")


@dp.message(Register.fullname)
async def register_fullname(message: types.Message, state: FSMContext):
    await state.update_data(fullname=message.text)
    await state.set_state(Register.image)
    await message.answer(f"<b>Rasmingizni yuboring:</b>")


@dp.message(Register.image and F.photo)
async def register_image(message: types.Message, state: FSMContext, bot: Bot):
    await state.update_data(user_id=message.from_user.id)
    photo = message.photo[-1]
    photo_info = await bot.get_file(photo.file_id)
    user_id = message.from_user.id
    file_path = f'https://api.telegram.org/file/bot{TOKEN}/{photo_info.file_path}'
    response = requests.get(file_path)

    if response.status_code == 200:
        save_directory = 'photos'
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        save_path = os.path.join(save_directory, f"{user_id}" + '.jpg')

        with open(save_path, 'wb') as f:
            f.write(response.content)

        # Yuzlarni aniqlash uchun haarcascades faylini yuklash
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Rasmni yuklash
        image_path = f'photos/{user_id}.jpg'  # Bu yerda o'zingizning rasm manzilingizni kiriting
        img = cv2.imread(image_path)

        # Rasm yuklanganligini tekshirish
        if img is None:
            await message.answer(
                f"<b>Rasm yuklanmadi. Iltimos, '{image_path}' yo'lini tekshiring va qayta yuboring ❌</b>")
        else:
            # Rasmni kulrang formatga o'zgartirish
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Yuzlarni aniqlash
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            photo_valid = True
            # Natijalarni ko'rsatish
            if len(faces) > 1:
                photo_valid = False
                await message.answer(f"<b>{len(faces)} ta yuz topildi!\nQayta yuboring ❌</b>")
            elif len(faces) == 1:
                photo_valid = True
                await message.answer("<b>Rasm yuklandi ✅</b>")
            else:
                photo_valid = False
                await message.answer("<b>Hech qanday yuz topilmadi.\nQayta yuboring ❌</b>")

            # Yuzlarni belgilash va rasmni ko'rsatish
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Natijaviy rasmni ko'rsatish
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            await state.set_state(Register.finish)
            data = await state.get_data()
            if photo_valid == True:
                fullname = data.get("fullname", "Unknown")
                user_id = data.get("user_id", "Unknown")
            else:
                ...

            def create_user(fullname, user_id):
                url = "http://127.0.0.1:8000/"
                response = requests.get(url=url).json()
                user_exist = False
                for i in response:
                    if i["user_id"] == user_id:
                        user_exist = True
                        break
                    elif i["fullname"] == fullname:
                        user_exist = True
                        break

                if user_exist == False:
                    photo_path = f"../PostBot/photos/{user_id}.jpg"
                    with open(photo_path, "rb") as file:
                        photo = {"image": file}
                        response_post = requests.post(url=url, files=photo, data={
                            "fullname": fullname,
                            "user_id": user_id
                        })
                        print(response_post.json())
                        return "Success created ✅"



                else:
                    return "Already exist user ❌"

            print(create_user(fullname, user_id))

            await message.answer("<b>Success created ✅</b>")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await bot.set_my_commands([
        BotCommand(command="start", description="Boshlash uchun bosing")
    ])
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
