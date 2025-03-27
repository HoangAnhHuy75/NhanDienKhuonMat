-Vào build_dataset.py run
-Nhập tên của mình từ cổng console, nhấn phím s để chụp ảnh từ video, chụp từ 10 đến 20 ảnh, sau đó nhấn phím q để thoát video
-Ảnh sẽ được lưu vào thư mục dataset

-Vào encode_faces.py run, đợi mã hóa hết tất cả ảnh trong thư mục dataset
-encode_faces dựa trên mô hình phát hiện khuôn mặt HOG của thư viện face_recognition dùng để mã hóa khuôn mặt 
-HOG là một thuật toán trích xuất đặc trưng từ hình ảnh bằng cách đếm số lượng gradient (độ dốc) theo các hướng khác nhau.
Cách hoạt động của HOG:
+Chia ảnh thành các ô nhỏ (cell) và khối (block).
+Tính toán hướng của gradient cho từng pixel.
+Xây dựng biểu đồ (histogram) của các hướng gradient trong từng ô.
+Chuẩn hóa dữ liệu và sử dụng nó làm đầu vào cho một bộ phân loại (SVM) để xác định xem có khuôn mặt hay không.
-Sử dụng FaceNet (Deep Learning) để tạo ra vector 128 chiều đại diện cho khuôn mặt
-Vào recognize_faces_video run, hệ thống sẽ nhận diện khuôn mặt và hiện ra tên của mình