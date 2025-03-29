import cv2
import os
from tkinter import messagebox
def build_dataset(t1,t2):
    if t1=="" or t2=="":
        messagebox.showinfo("Error","Vui lòng nhập đầy đủ thông tin")
    # khởi tạo đường dẫn vào trong thư mục dataset
    else:
        output_path = os.path.join("dataset",f"{t1}_{t2.strip()}")
        os.makedirs(output_path)
        # mở webcam
        video = cv2.VideoCapture(0)
        totalImage = 0
        while True:
            # đọc khung hình frame với câu lệnh video.read
            ret, frame = video.read()
            # show webcam lên màn hình
            cv2.imshow("My Video", frame)
            # cho khung hình chạy liên tục trong 1ms
            key = cv2.waitKey(1)
            # nếu nhấn phím s sẽ chụp ảnh
            if key == ord("s"):
                p = os.path.join(output_path, f"{str(totalImage).zfill(5)}.png")
                cv2.imwrite(p, frame)
                totalImage += 1
                print("Đã lưu ", totalImage, " ảnh")
            # nhấn phím q sẽ thoát video
            elif key == ord("q"):
                print("Tổng cộng : ", totalImage, " ảnh đã được lưu")
                break
        video.release()
        cv2.destroyAllWindows()




        
    
