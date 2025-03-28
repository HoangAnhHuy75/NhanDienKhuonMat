import cv2
import os
name=input("Hãy nhập tên của bạn : ").strip()
#khởi tạo đường dẫn vào trong thư mục dataset
output_path=os.path.join("dataset",name)
os.makedirs(output_path)
#mở webcam
video=cv2.VideoCapture(0)
totalImage=0
while True:
    #đọc khung hình frame với câu lệnh video.read
    ret,frame=video.read()
    #show webcam lên màn hình
    cv2.imshow("My Video",frame)
    #cho khung hình chạy liên tục trong 1ms
    key= cv2.waitKey(1)
    #nếu nhấn phím s sẽ chụp ảnh
    if key == ord("s"):
        p=os.path.join(output_path,f"{str(totalImage).zfill(5)}.png")
        cv2.imwrite(p,frame)
        totalImage+=1
        print("Đã lưu ",totalImage," ảnh")
    #nhấn phím q sẽ thoát video
    elif key== ord("q"):
        print("Tổng cộng : ",totalImage," ảnh đã được lưu")
        break
video.release()
cv2.destroyAllWindows()
        
    
