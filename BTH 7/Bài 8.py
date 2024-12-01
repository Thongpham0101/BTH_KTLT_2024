def write_list_to_file(file_path, data_list):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for item in data_list:
                file.write(f"{item}\n")  # Ghi từng phần tử trên một dòng
        print(f"Dữ liệu đã được ghi vào tệp: {file_path}")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi ghi vào tệp: {e}")

# Ví dụ danh sách
data = ["Dòng 1", "Dòng 2", "Dòng 3", "Dòng 4"]

# Đường dẫn đến tệp văn bản
file_path = "duong_dan_den_tep.txt"  # Thay bằng đường dẫn thực tế
write_list_to_file(file_path, data)
