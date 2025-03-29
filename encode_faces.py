import cv2
import os
import sys
import face_recognition
from imutils import paths
import pickle

# Kiểm tra thư mục dataset có tồn tại không
def encode_faces():
    if not os.path.exists("dataset"):
        print(f"[ERROR] Thư mục dataset không tồn tại. Hãy kiểm tra lại!")
        sys.exit(1)
    print(f"[INFO] Dữ liệu ảnh sẽ được lấy từ: dataset")
    print(f"[INFO] Encodings sẽ được lưu vào: encodings.pickle")
    # Lấy danh sách ảnh từ dataset
    imagePaths = list(paths.list_images("dataset"))

    if len(imagePaths) == 0:
        print("[ERROR] Không tìm thấy ảnh nào trong thư mục dataset.")
        sys.exit(1)

    knownEncodings = []
    knownNames = []

    for (i, imagePath) in enumerate(imagePaths):
        print(f"[INFO] Đang xử lý ảnh {i + 1}/{len(imagePaths)}: {imagePath}")

        name = os.path.basename(os.path.dirname(imagePath))
        image = cv2.imread(imagePath)

        if image is None:
            print(f"[ERROR] Không thể đọc ảnh: {imagePath}, bỏ qua...")
            continue

        # Kiểm tra số kênh màu, nếu chỉ có 1 kênh (grayscale) thì chuyển sang RGB
        if len(image.shape) == 2:
            print(f"[WARNING] Ảnh {imagePath} là grayscale, chuyển sang RGB...")
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        try:
            boxes = face_recognition.face_locations(rgb, model="hog")
            encodings = face_recognition.face_encodings(rgb, boxes)

            if len(encodings) == 0:
                print(f"[WARNING] Không phát hiện được khuôn mặt trong ảnh: {imagePath}, bỏ qua...")
                continue

            for encoding in encodings:
                knownEncodings.append(encoding)
                knownNames.append(name)

        except Exception as e:
            print(f"[ERROR] Lỗi xử lý ảnh {imagePath}: {str(e)}")

    if len(knownEncodings) == 0:
        print("[ERROR] Không có encodings nào được tạo. Hãy kiểm tra lại dataset.")
        sys.exit(1)

    print(f"[INFO] Đang lưu encodings vào file: encodings.pickle")
    data = {"encodings": knownEncodings, "names": knownNames}

    with open("encodings.pickle", "wb") as f:
        pickle.dump(data, f)

    print("[INFO] Quá trình mã hóa hoàn tất!")

