def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print("Tệp không tồn tại. Vui lòng kiểm tra lại đường dẫn.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Đường dẫn đến tệp văn bản
file_path = "duong_dan_den_tep.txt"  # Thay bằng đường dẫn thực tế
line_count = count_lines_in_file(file_path)
if line_count is not None:
    print(f"Số dòng trong tệp: {line_count}")
