#a)Xây dựng các radio button cho phép thực hiện các lựa chọn khác nhau:
import tkinter as tk
# Tạo cửa sổ chính
root = tk.Tk()
root.title("Choose Your Favorite Language")
# Khởi tạo biến
v = tk.IntVar()
v.set(1)  # Khởi tạo lựa chọn mặc định
# Danh sách các ngôn ngữ lập trình
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

def ShowChoice():
    print(v.get())
# Tạo nhãn
tk.Label(root, 
         text="Choose your favourite programming language:", 
         justify=tk.LEFT, 
         padx=20).pack()
# Tạo các radio button
for val, language in enumerate(languages):
    tk.Radiobutton(root, 
                   text=language[0], 
                   padx=20, 
                   variable=v, 
                   command=ShowChoice, 
                   value=language[1]).pack(anchor=tk.W)
# Chạy vòng lặp chính
root.mainloop()
#b)Thay thế các radio button thành các indicator như hình:
import tkinter as tk
# Tạo cửa sổ chính
root = tk.Tk()
root.title("Choose Your Favorite Language")
# Khởi tạo biến
v = tk.IntVar()
v.set(1)  # Khởi tạo lựa chọn mặc định
# Danh sách các ngôn ngữ lập trình
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

def ShowChoice():
    print(v.get())
# Tạo nhãn
tk.Label(root, 
         text="Choose your favourite programming language:", 
         justify=tk.LEFT, 
         padx=20).pack()
# Tạo các radio button với indicator
for val, language in enumerate(languages):
    tk.Radiobutton(root, 
                   text=language[0], 
                   indicatoron=0, 
                   width=20, 
                   padx=20, 
                   variable=v, 
                   command=ShowChoice, 
                   value=language[1]).pack(anchor=tk.W)
# Chạy vòng lặp chính
root.mainloop()
