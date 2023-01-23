import os.path
import sys
import face_recognition


def train_model_by_img():
    if not os.path.exists("media"):
        print("Директории няма!")
        sys.exit()
    #
    known_encodings = []
    images = os.listdir("media")

    for (i, image) in enumerate(images):
        # print(f"[+] processing img {i + 1}/{len(images)}")

        face_img = face_recognition.load_image_file(f"media/{image}")
        face_encoding = face_recognition.face_encodings(face_img)[0]
        # print(known_encodings)
        if len(known_encodings) == 0:
            known_encodings.append(face_encoding)
        else:
            for item in range(0, len(known_encodings)):
                result = face_recognition.compare_faces([face_encoding], known_encodings[item])

                if result[0]:
                    known_encodings.append(face_encoding)
                    # print("Одно лицо!")
                    break
                else:
                    # print("Другое лицо!")
                    break
    data = known_encodings

    return data
