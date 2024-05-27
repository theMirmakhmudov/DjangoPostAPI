# import requests
#
#
# def create_user(fullname, user_id):
#     url = "http://127.0.0.1:8000/"
#     response = requests.get(url=url).json()
#     user_exist = False
#     for i in response:
#         if i["user_id"] == user_id:
#             user_exist = True
#             break
#
#     if user_exist == False:
#         photo_path = "../media/images/aa.jpg"
#         with open(photo_path, "rb") as file:
#             photo = {"image": file}
#             response_post = requests.post(url=url, files=photo, data={
#                 "fullname": fullname,
#                 "user_id": user_id
#             })
#             print(response_post.json())
#             return "Success"
#
#     else:
#         return "Already exist user"
#
#
# print(create_user("Torabekov_08", 1747966069))
#
# # file_path = "aa.jpg"
# # url = "http://127.0.0.1:8000/"
# # with open(file_path, 'rb') as file:
# #     files = {"image": file}
# #     response = requests.post(url=url, files=files, data={
# #         'fullname': "Torabekov_08",
# #         'user_id': 56738292
# #     })
# # print(response.json())
from PostBot.main import db

# import cv2
#
# # Yuzlarni aniqlash uchun haarcascades faylini yuklash
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#
# # Rasmni yuklash
# image_path = 'photos/1747966069.jpg'  # Bu yerda o'zingizning rasm manzilingizni kiriting
# img = cv2.imread(image_path)
#
# # Rasm yuklanganligini tekshirish
# if img is None:
#     print(f"Rasm yuklanmadi. Iltimos, '{image_path}' yo'lini tekshiring.")
# else:
#     # Rasmni kulrang formatga o'zgartirish
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     # Yuzlarni aniqlash
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#
#     # Natijalarni ko'rsatish
#     if len(faces) > 0:
#         print(f"{len(faces)} ta yuz topildi!")
#     else:
#         print("Hech qanday yuz topilmadi.")
#
#     # Yuzlarni belgilash va rasmni ko'rsatish
#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#
#     # Natijaviy rasmni ko'rsatish
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

for user in db.get_ids_users:
    print(user[0])
