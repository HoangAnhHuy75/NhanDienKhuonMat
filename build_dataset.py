import cv2
import os
import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
window.title("Face Recognition")
window.geometry("1000x600")
window.configure(bg="#2C3E50")
title_label=tk.Label(window,text="Face Recognition System",
                     fg="white",font=("Arial",18,"bold"),bg="#2C3E50")
title_label.pack(pady=20)
def build_dataset():
    if t1.get()=="" or t2.get()=="":
        messagebox.showinfo("Error","Vui lòng nhập đầy đủ thông tin")
    # khởi tạo đường dẫn vào trong thư mục dataset
    else:
        output_path = os.path.join("dataset",f"{t1.get()}_{t2.get().strip()}")
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
frame=tk.Frame(window,bg="#34495E")
frame.pack(pady=30,fill="both",expand=True)

l1=tk.Label(frame,text="Enter ID : ",font=("Arial",16,"bold"),fg="white",bg="#34495E")
l1.grid(row=0,column=0,pady=20,padx=10)
t1=tk.Entry(frame,width=25,font=("Arial",16))
t1.grid(row=0,column=1)


l2=tk.Label(frame,text="Enter Name : ",font=("Arial",16,"bold"),bg="#34495E", fg="white")
l2.grid(row=1,column=0,padx=10,pady=20)
t2=tk.Entry(frame,width=25,font=("Arial",16))
t2.grid(row=1,column=1)
b1=tk.Button(frame,text="Tạo dataset",font=("Arial",16),bg="orange",fg="white",command=build_dataset)
b1.grid(row=2,column=0,pady=20,padx=10)


window.mainloop()




        
    
