# Mở tệp ở chế độ đọc
with open('D:/a.txt', 'r') as file:
    char, wc, lc = 0, 0, 0  # Khởi tạo các biến đếm: ký tự, từ, dòng
    
    # Duyệt qua từng dòng trong tệp
    for line in file:  
        char += len(line)  # Đếm số ký tự trong dòng (bao gồm cả khoảng trắng và xuống dòng)
        wc += len(line.split())  # Đếm số từ bằng cách tách dòng thành các từ dựa trên khoảng trắng
        lc += 1  # Tăng số dòng lên 1 mỗi khi đọc 1 dòng

# Hiển thị kết quả
print("Số ký tự là: %d" % char)
print("Số từ là: %d" % wc)
print("Số dòng là: %d" % lc)
