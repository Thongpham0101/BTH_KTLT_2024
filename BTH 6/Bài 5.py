class PySolution:
    def reverse_words(self, s):
        # Tách chuỗi thành các từ, đảo ngược thứ tự, và ghép lại thành chuỗi
        return ' '.join(reversed(s.split()))

# Tạo đối tượng và sử dụng
solution = PySolution()

# Đầu vào phải được đặt trong dấu nháy
input_string = "hello .py"
output = solution.reverse_words(input_string)

# In kết quả
print(output)  # Kết quả: '.py hello'
