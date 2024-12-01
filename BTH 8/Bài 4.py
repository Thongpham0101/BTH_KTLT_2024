#a) Xây dựng cửa sổ đồ họa window form:
from tkinter import *
# Tạo cửa sổ chính
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
#b) Thêm một widget (button) vào window form:
# Thêm một nhãn (label)
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
# Thêm một button với màu nền và màu chữ tùy chỉnh
btn = Button(window, text="Click Me", bg="blue", fg="white")
btn.grid(column=1, row=0)
#c) Xây dựng phương thức xử lý sự kiện phím bấm:
# Định nghĩa phương thức xử lý sự kiện phím bấm
def clicked():
    lbl.configure(text="Button was clicked !!")
# Gắn phương thức xử lý sự kiện vào button
btn.configure(command=clicked)
#d) Hoàn thiện và chạy ứng dụng:
# Chạy vòng lặp chính để hiển thị cửa sổ
window.mainloop()
