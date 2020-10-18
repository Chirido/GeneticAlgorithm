# GeneticAlgorithm
Thuật toán di truyền áp dụng cho tìm nghiệm phương trình bậc 2<br />
CÁC BƯỚC THỰC HIỆN:<br />
B1: Chọn quần thể với 100 cá thể ban đầu(phải tìm khoảng nghiệm để xác định quần thể) , nhập vào độ chính xác mong muốn<br />
B2: Cho hàm thích nghi và tính độ thích nghi của từng cá thể => hàm thích nghi: abs(A*x^2+B*x+C)<br />
B3: Sắp xếp các cá thể theo độ thích nghi tăng dần => Nếu có cá thể có độ thích nghi nhỏ hơn hoặc bằng độ chính xác đưa ra thì chọn cá thể đó là đáp án<br />
B4: Chọn phần tử lai ghép => chọn 50 cá thể đầu tiên (các cá thể tốt nhất)<br />
B5: Lai ghép tạo thành 100 cá thể đời con mới(nối chéo hai đoạn bit) => Dùng hàm bin_to_float và float_to_bin<br />
B6: Quay lại B2, tiếp tục quy trình và dừng khi có đáp án hoặc đã lai ghép quá 20 đời con và chuyển sang B7<br />
B7: Nếu lai ghép quá 20 đời con mà vẫn chưa tìm ra nghiệm thì đột biến và quay lại B2 => Tăng khoảng nghiệm để xét<br />
B8: Chọn đáp án <br />
