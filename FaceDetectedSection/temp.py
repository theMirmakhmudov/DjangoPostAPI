import requests
from datetime import datetime


def send_msg_arrived(user_id):
    TOKEN = "7128525968:AAEIm_z4nmgDHI7Sj7sM5y2w9jCbW6lG75o"

    photo_path = "../media/saved_images/Camera_detect_face.jpg"
    photo = {"photo": open(photo_path, "rb")}
    caption = f"<b>Farzandingiz maktabga yetib keldi ✅</b>\n📆 {datetime.now().strftime('<b>%d/%m/%y</b>')}\n⏰ {datetime.now().strftime('<b>%H : %M : %S</b>')}"
    user_id = user_id
    url_req = f"https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={user_id}&caption={caption}&parse_mode=HTML"
    response = requests.get(url_req, files=photo)
    print(response.json())


def send_msg_leave(user_id):
    TOKEN = "7128525968:AAEIm_z4nmgDHI7Sj7sM5y2w9jCbW6lG75o"

    photo_path = "../media/saved_images/Camera_detect_face.jpg"
    photo = {"photo": open(photo_path, "rb")}
    caption = f"Farzandingiz maktabdan chiqib ketdi ❗️\n📆 {datetime.now().strftime('<b>%d/%m/%y</b>')}\n⏰ {datetime.now().strftime('<b>%H : %M : %S</b>')}"
    user_id = user_id
    url_req = f"https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={user_id}&caption={caption}&parse_mode=HTML"
    response = requests.get(url_req, files=photo)
    print(response.json())
