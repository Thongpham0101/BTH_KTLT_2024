# Hàm đọc n dòng đầu tiên của tệp
def read_first_n_lines(file_path, n):
    from itertools import islice  # Nhập thư viện islice từ itertools
    with open(file_path, 'r') as f:  # Mở tệp ở chế độ đọc
        for line in islice(f, n):  # Dùng islice để đọc n dòng đầu tiên
            print(line.strip())  # In ra từng dòng, loại bỏ ký tự xuống dòng thừa

# Gọi hàm để đọc 2 dòng đầu tiên của tệp 'test.txt'
read_first_n_lines('test.txt', 2)
