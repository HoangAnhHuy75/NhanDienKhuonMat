import face_recognition
import pickle
import cv2
import time
import imutils
import os
from datetime import datetime

# Danh sách lưu thông tin nhận diện
recognized_data = []

def recognize_faces_video():
    global recognized_data

    if not os.path.exists("encodings.pickle"):
        print(f"[ERROR] File encodings.pickle không tồn tại. Hãy kiểm tra lại đường dẫn!")
        return

    print("[INFO] Đang tải encodings...")
    data = pickle.loads(open("encodings.pickle", "rb").read())

    print("[INFO] Khởi động camera...")
    video = cv2.VideoCapture(0)
    video.set(3, 1000)
    video.set(4, 800)

    time.sleep(2.0)

    while True:
        ret, frame = video.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb = imutils.resize(rgb, width=750)
        r = frame.shape[1] / float(rgb.shape[1])

        boxes = face_recognition.face_locations(rgb, model="hog")
        encodings = face_recognition.face_encodings(rgb, boxes)
        names = []

        for encoding in encodings:
            matches = face_recognition.compare_faces(data["encodings"], encoding)
            name = "Unknown"

            if True in matches:
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}
                for i in matchedIdxs:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0) + 1
                name = max(counts, key=counts.get)

            names.append(name)

        for ((top, right, bottom, left), name) in zip(boxes, names):
            top, right, bottom, left = int(top * r), int(right * r), int(bottom * r), int(left * r)
            display_text = name if name != "Unknown" else "Unknown"

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(frame, display_text, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow("Video", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            for name in names:
                if name != "Unknown":
                    user_id, user_name = name.split("_", 1)
                    now = datetime.now().strftime("%H:%M:%S %d-%m-%Y")
                    recognized_data.append([user_id, user_name, now])
            break

    video.release()
    cv2.destroyAllWindows()
