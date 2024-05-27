import asyncio
import logging
import os

import requests
from aiogram import Dispatcher, F, types
from aiogram.enums import ParseMode, MessageEntityType, ContentType
from aiogram.filters import Command
from aiogram import Bot
from aiogram.types import BotCommand, BufferedInputFile
from dotenv import load_dotenv
from aiogram.fsm.context import FSMContext
from states import Register, AdminAdvertisement
import cv2
from buttons import admin
from db import Database

load_dotenv(".env")
TOKEN = os.getenv("TOKEN")
Admin = os.getenv("Admin")
Channel = os.getenv("CHANNEL")
DB = os.getenv("DB_NAME")
dp = Dispatcher()
db = Database(f"../db.sqlite3")


@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext, bot: Bot):
    if message.from_user.id == int(Admin):
        await message.answer("<b>Admin panelga xush kelibsiz 🧑‍💻</b>", reply_markup=admin)
        bot_info = await bot.get_me()

        @dp.message(F.text == "Reklama yuborish 📢")
        async def send_advertisement(message: types.Message, state: FSMContext):
            await state.set_state(AdminAdvertisement.photo)
            await message.answer("<b>Reklamaning rasmini yuboring 🖼</b>", reply_markup=types.ReplyKeyboardRemove())

        @dp.message(AdminAdvertisement.photo and F.document)
        async def send_advertisement_photo(message: types.Message, state: FSMContext, bot: Bot):

            if F.document:
                docs = message.document
                document_info = await bot.get_file(docs.file_id)
                file_path = f'https://api.telegram.org/file/bot{TOKEN}/{document_info.file_path}'
                response = requests.get(file_path)

                if response.status_code == 200:
                    save_directory = 'photos'
                    if not os.path.exists(save_directory):
                        os.makedirs(save_directory)

                    save_path = os.path.join(save_directory, "Advertisement_photo" + '.jpg')

                    with open(save_path, 'wb') as f:
                        f.write(response.content)
                        print("Saqlandi  ✅")
                        await state.set_state(AdminAdvertisement.caption)
                        await message.answer("<b>Reklamaning matnini kiriting:</b>")

                else:
                    print("Saqlanmadi ❌")

            @dp.message(AdminAdvertisement.photo and F.entities[:].type == MessageEntityType.URL)
            async def send_advertisement_photo(message: types.Message, state: FSMContext):
                if F.entities[:].type == MessageEntityType.URL:
                    await state.update_data(photo=message.text)
                    await message.answer("<b>Reklamaning matnini kiriting:</b>")
                    await state.set_state(AdminAdvertisement.caption)
                else:
                    print("Xatolik ❌")

            @dp.message(AdminAdvertisement.caption)
            async def send_advertisement_caption(message: types.Message, state: FSMContext, bot: Bot):
                await state.update_data(caption=message.text)
                await state.set_state(AdminAdvertisement.finish)
                await state.set_state(AdminAdvertisement.finish)
                data = await state.get_data()
                await state.clear()
                photo = data.get("photo", "Unknown")
                caption = data.get("caption", "Unknown")

                await message.answer("<b>📢 Reklama jo'natish boshlandi...</b>")
                for user in db.get_ids_users:
                    if photo == "Unknown":
                        photo_path = "photos/Advertisement_photo.jpg"
                        with open(photo_path, 'rb') as photo_file:
                            photo = BufferedInputFile(photo_file.read(), filename='photo.jpg')
                            await bot.send_photo(chat_id=user[0], photo=photo,
                                                 caption=f"<b>{caption}\n🤖 {bot_info.mention_html()}</b>")

                    elif photo != "Unknown":
                        await bot.send_photo(chat_id=user[0], photo=photo,
                                             caption=f"<b>{caption}\n\n🤖 {bot_info.mention_html()}</b>")

                    else:
                        print("Reklama yuborishda xatolik !")
                await message.answer(f"<b>Reklama yuborish yakunlandi ✅\n\n🤖 {bot_info.mention_html()}</b>")




    else:
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
        if message.photo:
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
                    print("Saqlandi ✅")
            else:
                await message.answer("Xabar turi Photo emas ❌")

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
                    await message.answer(f"<b>{len(faces)} ta yuz topildi!\nQayta yuboring ❌</b>")
                    photo_valid = False

                elif len(faces) == 1:
                    delete = await message.answer("<b>Photo successfully upload ✅</b>")
                    photo_valid = True

                else:
                    await message.answer("<b>Hech qanday yuz topilmadi.\nQayta yuboring ❌</b>")
                    photo_valid = False

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
                    bot_info_ = await bot.get_me()
                    await message.answer(
                        f"<b>Success created ✅\nFullname: {fullname}\nUser Id: {user_id}\nPhoto: {user_id}.jpg\n\n🤖 {bot_info_.mention_html()}</b>")
                    await bot.delete_message(chat_id=user_id, message_id=delete.message_id)
                elif photo_valid == False:
                    ...


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await bot.set_my_commands([
        BotCommand(command="start", description="Boshlash uchun bosing")
    ])
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
