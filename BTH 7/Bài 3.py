# Mở tệp và đọc toàn bộ nội dung
def read_full_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()  # Đọc toàn bộ nội dung tệp
    return content

# Gọi hàm với đường dẫn tệp
file_path = 'D:/a.txt'
print("Nội dung của tệp là:")
print(read_full_file(file_path))
