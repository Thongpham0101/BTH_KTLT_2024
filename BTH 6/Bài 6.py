class IOString:
    def __init__(self):
        # Khởi tạo thuộc tính str1 là một chuỗi rỗng
        self.str1 = ""

    def get_String(self):
        # Nhập chuỗi từ người dùng
        self.str1 = input("Nhập một chuỗi: ")

    def print_String(self):
        # In chuỗi đã nhập dưới dạng chữ in hoa
        print(self.str1.upper())

# Sử dụng class
str1 = IOString()      # Tạo đối tượng của class IOString
str1.get_String()      # Nhận chuỗi từ người dùng
str1.print_String()    # In chuỗi dưới dạng chữ in hoa
