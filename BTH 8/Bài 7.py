# import các thư viện cần thiết
import tkinter
import random

# danh sách các màu có thể có
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0

# Bước 2: Thay đổi thời gian chơi từ 30 giây thành 120 giây
timeleft = 120

# Bước 1: Viết chương trình game học các màu tiếng anh
# hàm bắt đầu trò chơi
def startGame(event):
    global timeleft
    if timeleft == 120:
        # bắt đầu đếm ngược thời gian
        countdown()
    # chạy hàm để chọn màu tiếp theo
    nextColour()

# hàm để chọn và hiển thị màu tiếp theo
def nextColour():
    global score
    global timeleft

    # nếu trò chơi đang diễn ra
    if timeleft > 0:
        # kích hoạt hộp nhập văn bản
        e.focus_set()
        
        # Bước 3: Thay đổi số điểm cộng cho mỗi lần đoán đúng là 2, mỗi lần đoán sai là -1
        # nếu màu được nhập bằng với màu của văn bản
        if e.get().lower() == colours[1].lower():
            score += 2  # đoán đúng thì được cộng 2 điểm
        else:
            score -= 1  # đoán sai thì bị trừ 1 điểm
        
        # xóa nội dung của hộp nhập văn bản
        e.delete(0, tkinter.END)
        
        random.shuffle(colours)
        
        # thay đổi màu sắc để nhập bằng cách thay đổi văn bản và màu thành giá trị màu ngẫu nhiên
        label.config(fg=str(colours[1]), text=str(colours[0]))
        
        # cập nhật điểm số
        scoreLabel.config(text="Score: " + str(score))

# hàm đếm ngược thời gian
def countdown():
    global timeleft

    # nếu trò chơi đang diễn ra
    if timeleft > 0:
        # giảm thời gian đi 1 giây
        timeleft -= 1
        
        # cập nhật nhãn thời gian còn lại
        timeLabel.config(text="Time left: " + str(timeleft))
        
        # chạy hàm này lại sau 1 giây
        timeLabel.after(1000, countdown)

# Mã chính

# tạo một cửa sổ GUI
root = tkinter.Tk()

# đặt tiêu đề
root.title("COLORGAME")

# đặt kích thước
root.geometry("375x200")

# thêm nhãn hướng dẫn
instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!", font=('Helvetica', 12))
instructions.pack()

# thêm nhãn điểm số
scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()

# thêm nhãn thời gian còn lại
timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

# thêm nhãn để hiển thị màu sắc
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# thêm hộp nhập văn bản để nhập màu
e = tkinter.Entry(root)

# chạy hàm 'startGame' khi nhấn phím Enter
root.bind('<Return>', startGame)
e.pack()

# đặt con trỏ vào hộp nhập văn bản
e.focus_set()

# bắt đầu GUI
root.mainloop()
