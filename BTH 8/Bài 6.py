from tkinter import *

# Bước 1: Thực hiện tạo mới window form và các menu theo code mẫu
def NewFile():
    print("New File!")

def OpenFile():
    print("Open File!")

def Exit():
    print("Exiting application...")
    root.quit()

def About():
    print("This is a simple example of a menu")

def InsText():
    print("Insert Text!")

def InsPic():
    print("Insert Picture!")

# Tạo cửa sổ chính
root = Tk()
root.title("Menu Example")
root.geometry("400x300")

# Bước 2: Tạo menu File và thêm các lệnh vào
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)

# Tạo menu Insert và thêm các lệnh vào
insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)

# Tạo menu Help và thêm lệnh About vào
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

# Bước 3: Thêm các phương thức OpenFile(), Exit(), InsText(), InsPic()
# để hiển thị các thông báo lựa chọn tương ứng

# Chạy vòng lặp chính để hiển thị cửa sổ
root.mainloop()
