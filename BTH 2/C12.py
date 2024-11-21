print("PHẠM MẠNH THỐNG")
print("MSV:235752021610071")
import re
#Nhập mật khẩu từ người dùng
a=input("Nhập mật khẩu: ") 
#Kiểm tra độ dài của mật khẩu
if len(a)<6 or len(a)>12:
    print("Mật khẩu phải lớn hơn 6 kí tự và nhỏ hơn 12 ký tự")
else:
    if not re.search("[0-9]",a):
        print("Mật khẩu phải chứa ít nhất 1 chữ số")
    elif not re.search("[A-Z]",a):
        print("Mật khẩu phải chứ ít nhất 1 ký tự viết hoa")
    elif not re.search("[a-z]",a):
        print("Mật khẩu phải chứ ít nhất 1 ký tự thường")
    elif not re.search("[!@#$%^&?]",a):
        print("Mật khẩu phải chứa ít nhất 1 ký tự đặc biệt")
    else:
        print("Xác nhận lại mật khẩu: ",a)

