def copy_file_content(source_file, target_file):
    try:
        # Mở tệp nguồn để đọc
        with open(source_file, 'r', encoding='utf-8') as src:
            content = src.read()
        
        # Mở tệp đích để ghi
        with open(target_file, 'w', encoding='utf-8') as tgt:
            tgt.write(content)
        
        print(f"Đã sao chép nội dung từ '{source_file}' sang '{target_file}'")
    except FileNotFoundError:
        print(f"Tệp nguồn '{source_file}' không tồn tại. Vui lòng kiểm tra lại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Đường dẫn tệp nguồn và tệp đích
source_file = "tep_nguon.txt"  # Thay bằng đường dẫn tệp nguồn
target_file = "tep_dich.txt"   # Thay bằng đường dẫn tệp đích

copy_file_content(source_file, target_file)
