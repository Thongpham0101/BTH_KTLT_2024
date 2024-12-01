# Mở tệp
input_file = open('C:/a.txt', 'r')  # Sửa tên biến 'input_fie' thành 'input_file'

# Duyệt qua từng dòng trong tệp
for line in input_file:
    line = line.strip()  # Loại bỏ khoảng trắng thừa hoặc ký tự xuống dòng ở cuối dòng
    l = len(line)  # Sửa lỗi 'ine' thành 'line'
    s = ''  # Khởi tạo chuỗi 's' là chuỗi rỗng
    while l >= 1:
        s = s + line[l - 1]  # Sửa lỗi logic để đảo ngược chuỗi
        l -= 1
    print(s)

# Đóng tệp
input_file.close()
