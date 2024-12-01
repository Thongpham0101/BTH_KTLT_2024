def find_longest_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()  # Tách nội dung thành danh sách các từ
            max_length = max(len(word) for word in words)  # Tìm độ dài lớn nhất của từ
            longest_words = [word for word in words if len(word) == max_length]  # Lọc các từ dài nhất
            
        return longest_words, max_length
    except FileNotFoundError:
        print("Tệp không tồn tại. Vui lòng kiểm tra lại đường dẫn.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Đường dẫn đến tệp văn bản
file_path = "duong_dan_den_tep.txt"  # Thay bằng đường dẫn thực tế

result = find_longest_words(file_path)
if result:
    longest_words, max_length = result
    print(f"Từ dài nhất có độ dài {max_length} ký tự: {', '.join(longest_words)}")
