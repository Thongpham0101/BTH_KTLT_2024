from tkinter import *

# Tạo cửa sổ chính
root = Tk()
root.title("Personal Information and Radio Buttons")

# Khung hiển thị thông tin cá nhân
frame_info = Frame(root)
frame_info.pack(side=TOP, fill=X)

Label(frame_info, text="Họ Tên:").grid(row=0, column=0, sticky=W)
Label(frame_info, text="Ngày tháng năm sinh:").grid(row=1, column=0, sticky=W)
Label(frame_info, text="MSSV:").grid(row=2, column=0, sticky=W)
Label(frame_info, text="Ngành học:").grid(row=3, column=0, sticky=W)

Label(frame_info, text="Phạm Mạnh Thống").grid(row=0, column=1, sticky=W)
Label(frame_info, text="01/01/2005").grid(row=1, column=1, sticky=W)
Label(frame_info, text="235752021610071").grid(row=2, column=1, sticky=W)
Label(frame_info, text="KTĐK&TĐH").grid(row=3, column=1, sticky=W)

# Khung chứa các nút radio button
frame_radio = Frame(root)
frame_radio.pack(side=TOP, fill=X, pady=10)

# Biến lưu trữ giá trị nút radio button
v = IntVar()
v.set(1)  # Khởi tạo giá trị mặc định

# Hàm hiển thị lựa chọn
def show_choice():
    print(f"Bạn đã chọn số {v.get()}")

Label(frame_radio, text="Lựa chọn số:").pack(anchor=W)
Radiobutton(frame_radio, text="Số 1", variable=v, value=1).pack(anchor=W)
Radiobutton(frame_radio, text="Số 2", variable=v, value=2).pack(anchor=W)
Radiobutton(frame_radio, text="Số 3", variable=v, value=3).pack(anchor=W)
Button(frame_radio, text="Click Me", command=show_choice).pack()

# Chạy vòng lặp chính để hiển thị cửa sổ
root.mainloop()
