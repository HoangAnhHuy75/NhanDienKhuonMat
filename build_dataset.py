import os
import cv2
from tkinter import messagebox


def build_dataset(t1, t2):
    if t1 == "" or t2 == "":
        messagebox.showinfo("Error", "Vui lòng nhập đầy đủ thông tin")
        return
    else:
        folder_name = f"{t1}_{t2.strip()}"
        output_path = os.path.join("dataset", folder_name)

        # Kiểm tra các thư mục con trong dataset
        if os.path.exists("dataset"):
            for folder in os.listdir("dataset"):
                # Tách phần ID ra kiểm tra (ID là t1)
                existing_id = folder.split("_")[0]
                if existing_id == t1.strip():
                    messagebox.showerror("Error", f"ID {t1} đã tồn tại ! Vui lòng nhập ID khác.")
                    return
        try:
            os.makedirs(output_path)
        except Exception as e:
            messagebox.showerror("Error", f"Không thể tạo thư mục: {e}")
            return
        # mở webcam
        video = cv2.VideoCapture(0)
        if not video.isOpened():
            messagebox.showerror("Error", "Không thể mở webcam")
            return
        totalImage = 0
        while True:
            ret, frame = video.read()
            if not ret:
                messagebox.showerror("Error", "Không thể đọc frame từ webcam")
                break

            cv2.imshow("My Video", frame)
            key = cv2.waitKey(1)

            if key == ord("s"):
                p = os.path.join(output_path, f"{str(totalImage).zfill(5)}.png")
                cv2.imwrite(p, frame)
                totalImage += 1
                print("Đã lưu ", totalImage, " ảnh")
            elif key == ord("q"):
                print("Tổng cộng: ", totalImage, " ảnh đã được lưu")
                break

        video.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Info", f"Đã lưu {totalImage} ảnh tại {output_path}")
