# # from datetime import datetime
# #
# # import cv2
# # import os
# # import face_recognition
# # from temp import send_msg_arrived, send_msg_leave
# #
# #
# # def load_and_process_image(image_path):
# #     # Tasvirni yuklash
# #     image = cv2.imread(image_path)
# #
# #     # Tasvirni muvaffaqiyatli yuklanganligini tekshirish
# #     if image is None:
# #         raise ValueError(f"Tasvirni yuklashda xatolik: {image_path}")
# #
# #     # Tasvirni RGB formatiga o'tkazish
# #     rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# #     # Yuzlarni aniqlash
# #     face_locations = face_recognition.face_locations(rgb_image)
# #     if len(face_locations) == 0:
# #         return None
# #     else:
# #         return face_recognition.face_encodings(rgb_image)
# #
# #
# # # Kompyuterdagi rasmlar ro'yxati
# # image_path = "../media/images/"
# # image_list = os.listdir(image_path)
# #
# # # Kompyuter kamerasidan tasvir olish
# # video_capture = cv2.VideoCapture(0)
# #
# # # Kamerani ochish uchun tekshirish
# # if not video_capture.isOpened():
# #     print("Kamera ochilmayapti. Kamerani tekshiring yoki dasturni qayta ishga tushiring.")
# #     exit()
# #
# # print("Kamerani yoqib, rasmga olish uchun 'Enter' tugmasini bosing. Chiqish uchun 'q' tugmasini bosing.")
# #
# # while True:
# #     # Videodan tasvir olish
# #     ret, frame = video_capture.read()
# #
# #     # Tasvirni ko'rsatish
# #     cv2.imshow('Video', frame)
# #
# #     # Klaviatura tugmasini tekshirish
# #     key = cv2.waitKey(1) & 0xFF
# #
# #     # 'Enter' tugmasini bosganda tasvirni olish
# #     if key == 13:  # 13 - Enter tugmasi
# #         # Tasvirni olish
# #         ret, frame = video_capture.read()
# #         # Tasvirni RGB formatiga o'tkazish
# #         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# #         # Yuzni olish
# #         face_encodings = face_recognition.face_encodings(rgb_frame)
# #
# #         # Agar tasvirda yuz aniqlangan bo'lsa
# #         if face_encodings:
# #             # Agar bir nechta yuzlar aniqlangan bo'lsa
# #             if len(face_encodings) > 1:
# #                 print("Rasmda bir nechta yuzlar mavjud.")
# #                 print(f"Rasmda {len(face_encodings)} odam yuzi bor.")
# #             else:
# #                 print("Rasmda faqat bir ta yuz mavjud.")
# #                 found_match = False
# #
# #                 for image_name in image_list:
# #                     image_full_path = os.path.join(image_path, image_name)
# #                     try:
# #                         known_face_encodings = load_and_process_image(image_full_path)
# #                     except ValueError as e:
# #                         print(e)
# #                         continue
# #
# #                     if known_face_encodings is not None:
# #                         for face_encoding in face_encodings:
# #                             matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
# #                             if True in matches:
# #                                 found_match = True
# #                                 cv2.putText(frame, "Yuz mos keladi. ✅", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
# #                                             (0, 255, 0), 2, cv2.LINE_AA)
# #                                 print(f"{image_name}: Yuzlar bir xil.")
# #                                 save_path = "../media/saved_images/"
# #                                 if not os.path.exists(save_path):
# #                                     os.makedirs(save_path)
# #                                 filename = str("Camera_detect_face") + ".jpg"
# #                                 cv2.imwrite(os.path.join(save_path, filename), frame)
# #                                 print(f"Rasm saqlandi {filename}")
# #                                 image_name1 = os.path.basename(image_name)
# #                                 image_name_without_extension = os.path.splitext(image_name1)[0]
# #                                 if datetime.now().hour <= 8:
# #                                     send_msg_leave(user_id=image_name_without_extension)
# #                                     print(send_msg_leave)
# #                                 else:
# #                                     send_msg_leave(user_id=image_name_without_extension)
# #                                     print(send_msg_arrived)
# #
# #                                 break
# #                         if found_match:
# #                             break
# #
# #                 if not found_match:
# #                     print("Yuzlar bir xil emas.")
# #
# #
# #         else:
# #             print("Rasmda yuz aniqlanmadi yoki solishtirilgan yuz mavjud emas.")
# #             cv2.putText(frame, "Yuz mos emas. ❌", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
# #
# #     # 'q' tugmasini bosganda chiqish
# #     elif key == ord('q'):
# #         break
# #
# # # Kamerani to'xtatish va oynani yopish
# # video_capture.release()
# # cv2.destroyAllWindows()
#
#
# import cv2
# import os
# import face_recognition
# from datetime import datetime
# from temp import send_msg_arrived, send_msg_leave
#
#
# def load_and_process_image(image_path):
#     # Tasvirni yuklash
#     image = cv2.imread(image_path)
#     # Tasvirni muvaffaqiyatli yuklanganligini tekshirish
#     if image is None:
#         raise ValueError(f"Tasvirni yuklashda xatolik: {image_path}")
#     # Tasvirni RGB formatiga o'tkazish
#     rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     # Yuzlarni aniqlash
#     face_locations = face_recognition.face_locations(rgb_image)
#     if len(face_locations) == 0:
#         return None
#     else:
#         return face_recognition.face_encodings(rgb_image)
#
#
# def load_known_faces(image_dir):
#     known_faces = []
#     image_list = os.listdir(image_dir)
#     for image_name in image_list:
#         image_full_path = os.path.join(image_dir, image_name)
#         try:
#             encodings = load_and_process_image(image_full_path)
#             if encodings:
#                 known_faces.append((image_name, encodings))
#         except ValueError as e:
#             print(e)
#     return known_faces
#
#
# def recognize_face(frame, known_faces, tolerance=0.6):
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     face_encodings = face_recognition.face_encodings(rgb_frame)
#     for face_encoding in face_encodings:
#         for image_name, known_face_encodings in known_faces:
#             distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#             match_index = distances.argmin()
#             if distances[match_index] <= tolerance:
#                 return image_name
#     return None
#
#
# # Kompyuterdagi rasmlar ro'yxati
# image_path = "../media/images/"
# known_faces = load_known_faces(image_path)
#
# # Kompyuter kamerasidan tasvir olish
# video_capture = cv2.VideoCapture(0)
#
# # Kamerani ochish uchun tekshirish
# if not video_capture.isOpened():
#     print("Kamera ochilmayapti. Kamerani tekshiring yoki dasturni qayta ishga tushiring.")
#     exit()
#
# print("Kamerani yoqib, rasmga olish uchun 'Enter' tugmasini bosing. Chiqish uchun 'q' tugmasini bosing.")
#
# save_path = "../media/saved_images/"
#
# if not os.path.exists(save_path):
#     os.makedirs(save_path)
#
# while True:
#     # Videodan tasvir olish
#     ret, frame = video_capture.read()
#
#     # Tasvirni ko'rsatish
#     cv2.imshow('Video', frame)
#
#     # Klaviatura tugmasini tekshirish
#     key = cv2.waitKey(1) & 0xFF
#
#     # 'Enter' tugmasini bosganda tasvirni olish
#     if key == 13:  # 13 - Enter tugmasi
#         # Tasvirni olish
#         ret, frame = video_capture.read()
#
#         # Yuzni tanib olish
#         matched_image_name = recognize_face(frame, known_faces)
#
#         if matched_image_name:
#             print("Yuz mos keladi. ✅")
#             cv2.putText(frame, "Yuz mos keladi. ✅", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
#             image_name_without_extension = os.path.splitext(os.path.basename(matched_image_name))[0]
#             if datetime.now().hour <= 8:
#                 send_msg_leave(user_id=image_name_without_extension)
#                 print(send_msg_leave)
#             else:
#                 send_msg_arrived(user_id=image_name_without_extension)
#                 print(send_msg_arrived)
#         else:
#             print("Yuzlar bir xil emas.")
#             cv2.putText(frame, "Yuz mos emas. ❌", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
#
#         # Tasvirni ko'rsatish va 5 soniya davomida kutish
#         cv2.imshow('Video', frame)
#         cv2.waitKey(5000)  # 5000 ms = 5 soniya
#
#     # 'q' tugmasini bosganda chiqish
#     elif key == ord('q'):
#         break
#
# # Kamerani to'xtatish va oynani yopish
# video_capture.release()
# cv2.destroyAllWindows()



import cv2
import os
import face_recognition
from datetime import datetime
from temp import send_msg_arrived, send_msg_leave


def load_and_process_image(image_path):
    # Tasvirni yuklash
    image = cv2.imread(image_path)
    # Tasvirni muvaffaqiyatli yuklanganligini tekshirish
    if image is None:
        raise ValueError(f"Tasvirni yuklashda xatolik: {image_path}")
    # Tasvirni RGB formatiga o'tkazish
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Yuzlarni aniqlash
    face_locations = face_recognition.face_locations(rgb_image)
    if len(face_locations) == 0:
        return None
    else:
        return face_recognition.face_encodings(rgb_image)


def load_known_faces(image_dir):
    known_faces = []
    image_list = os.listdir(image_dir)
    for image_name in image_list:
        image_full_path = os.path.join(image_dir, image_name)
        try:
            encodings = load_and_process_image(image_full_path)
            if encodings:
                known_faces.append((image_name, encodings))
        except ValueError as e:
            print(e)
    return known_faces


# Kompyuterdagi rasmlar ro'yxati
image_path = "../media/images/"
known_faces = load_known_faces(image_path)

# Kompyuter kamerasidan tasvir olish
video_capture = cv2.VideoCapture(0)

# Kamerani ochish uchun tekshirish
if not video_capture.isOpened():
    print("Kamera ochilmayapti. Kamerani tekshiring yoki dasturni qayta ishga tushiring.")
    exit()

print("Kamerani yoqib, rasmga olish uchun 'Enter' tugmasini bosing. Chiqish uchun 'q' tugmasini bosing.")

save_path = "../media/saved_images/"

if not os.path.exists(save_path):
    os.makedirs(save_path)

while True:
    # Videodan tasvir olish
    ret, frame = video_capture.read()

    # Tasvirni ko'rsatish
    cv2.imshow('Video', frame)

    # Klaviatura tugmasini tekshirish
    key = cv2.waitKey(1) & 0xFF

    # 'Enter' tugmasini bosganda tasvirni olish
    if key == 13:  # 13 - Enter tugmasi
        # Tasvirni olish
        ret, frame = video_capture.read()
        # Tasvirni RGB formatiga o'tkazish
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Yuzni olish
        face_encodings = face_recognition.face_encodings(rgb_frame)

        # Agar tasvirda yuz aniqlangan bo'lsa
        if face_encodings:
            print("Rasmda faqat bir ta yuz mavjud.")
            found_match = False
            best_match_name = None
            best_match_distance = 1.0  # Initial high value

            for image_name, known_face_encodings in known_faces:
                for face_encoding in face_encodings:
                    distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = distances.argmin()
                    if distances[best_match_index] < best_match_distance:
                        best_match_distance = distances[best_match_index]
                        best_match_name = image_name

            if best_match_distance < 0.6:  # You can adjust this threshold
                found_match = True

            if found_match:
                print("Yuz mos keladi. ✅")
                cv2.putText(frame, "Yuz mos keldi.", (200, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                image_name_without_extension = os.path.splitext(os.path.basename(best_match_name))[0]
                # Tasvirni saqlash
                filename = str("Camera_detect_face") + ".jpg"
                cv2.imwrite(os.path.join(save_path, filename), frame)
                print(f"Rasm saqlandi {filename}")
                if datetime.now().hour <= 8:
                    send_msg_leave(user_id=image_name_without_extension)
                    print(send_msg_leave)
                else:
                    send_msg_arrived(user_id=image_name_without_extension)
                    print(send_msg_arrived)
            else:
                print("Yuzlar bir xil emas.")
                cv2.putText(frame, "Yuz mos emas.", (200, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)




            # Tasvirni ko'rsatish va 5 soniya davomida kutish
            cv2.imshow('Video', frame)
            cv2.waitKey(5000)  # 5000 ms = 5 soniya

        else:
            print("Rasmda yuz aniqlanmadi yoki solishtirilgan yuz mavjud emas.")
            cv2.putText(frame, "Rasmda yuz aniqlanmadi.", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

            # Tasvirni ko'rsatish va 5 soniya davomida kutish
            cv2.imshow('Video', frame)
            cv2.waitKey(5000)  # 5000 ms = 5 soniya

    # 'q' tugmasini bosganda chiqish
    elif key == ord('q'):
        break

# Kamerani to'xtatish va oynani yopish
video_capture.release()
cv2.destroyAllWindows()
