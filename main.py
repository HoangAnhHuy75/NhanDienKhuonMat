import cv2
import os
import tkinter as tk
from tkinter import messagebox
from build_dataset import build_dataset
from encode_faces import encode_faces
from recognize_faces_video import recognize_faces_video, recognized_data
from datetime import datetime

window = tk.Tk()
window.title("Face Recognition")
window.geometry("1000x600")
window.configure(bg="#2C3E50")

title_label = tk.Label(window, text="Face Recognition System",
                       fg="white", font=("Arial", 18, "bold"), bg="#2C3E50")
title_label.pack(pady=10)

def updateTime():
    now = datetime.now()
    dateTime = now.strftime("%H:%M:%S  %d-%m-%Y")
    time_label.config(text=dateTime)
    window.after(1000, updateTime)

frame = tk.Frame(window, bg="#34495E")
frame.pack(pady=20, fill="both", expand=True)

time_label = tk.Label(window, text="", font=("Arial", 12, "bold"), fg="white", bg="#2C3E50")
time_label.pack(after=title_label, pady=10)
updateTime()

l1 = tk.Label(frame, text="Enter ID : ", font=("Arial", 16, "bold"), fg="white", bg="#34495E")
l1.grid(row=0, column=0, pady=10, padx=10)
t1 = tk.Entry(frame, width=25, font=("Arial", 16))
t1.grid(row=0, column=1)

l2 = tk.Label(frame, text="Enter Name : ", font=("Arial", 16, "bold"), bg="#34495E", fg="white")
l2.grid(row=1, column=0, padx=10, pady=10)
t2 = tk.Entry(frame, width=25, font=("Arial", 16))
t2.grid(row=1, column=1)

b1 = tk.Button(frame, text="Tạo dataset", font=("Arial", 16), bg="orange", fg="white",
               command=lambda: build_dataset(t1.get(), t2.get()))
b1.grid(row=2, column=0, pady=10, padx=10)

b2 = tk.Button(frame, text="Mã hóa ảnh", font=("Arial", 16), bg="orange", fg="white", command=encode_faces)
b2.grid(row=2, column=1, pady=10, padx=20)

def run_recognition():
    recognize_faces_video()
    update_table()

b3 = tk.Button(frame, text="Nhận diện", font=("Arial", 16), bg="orange", fg="white", command=run_recognition)
b3.grid(row=2, column=2, pady=10, padx=20)

# Tạo bảng trong frame
table_frame = tk.Frame(frame, bg="#ECF0F1")
table_frame.grid(row=3, column=0, columnspan=3, pady=20, padx=10, sticky="nsew")

# Tiêu đề của bảng
headers = ["ID", "Name", "Time"]
for col, text in enumerate(headers):
    header_label = tk.Label(table_frame, text=text, font=("Arial", 14, "bold"), bg="#2C3E50", fg="white", width=15)
    header_label.grid(row=0, column=col, padx=5, pady=5, sticky="ew")

# Hàm cập nhật dữ liệu vào bảng
def update_table():
    for widget in table_frame.winfo_children():
        widget.destroy()

    for col, text in enumerate(headers):
        header_label = tk.Label(table_frame, text=text, font=("Arial", 14, "bold"), bg="#2C3E50", fg="white", width=15)
        header_label.grid(row=0, column=col, padx=5, pady=5, sticky="ew")

    for row, data in enumerate(recognized_data, start=1):
        for col, text in enumerate(data):
            data_label = tk.Label(table_frame, text=text, font=("Arial", 12), bg="white", fg="black", width=15)
            data_label.grid(row=row, column=col, padx=5, pady=5, sticky="ew")

window.mainloop()
