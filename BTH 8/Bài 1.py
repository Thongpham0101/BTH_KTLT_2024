#lệnh này nhập thư viện turtle,một thư viện hỗ trợ vẽ đồ họa python
import turtle

window = turtle.Screen()#window = turtle.Screen(): Tạo một cửa sổ hiển thị cho Turtle Graphics.
window.bgcolor("lightblue")#window.bgcolor("lightblue"): Thiết lập màu nền cho cửa sổ là màu xanh nước biển.

painter = turtle.Turtle()#Tạo một đối tượng Turtle mới có tên painter.
painter.fillcolor('red')#Thiết lập màu tô (fill) cho các hình vẽ của Turtle là màu đỏ.
painter.pencolor('red')#Thiết lập màu bút (pen) cho các đường vẽ của Turtle là màu đỏ.
painter.pensize(3)#Thiết lập độ dày của bút vẽ là 3 pixel.

def drawsq(t, s):#Hàm này vẽ một hình vuông.
    for i in range(4):
        t.forward(s)#Di chuyển Turtle về phía trước một khoảng s pixel.
        t.left(90)#Xoay Turtle sang trái 90 độ.

for i in range(1, 180):#Lặp 179 lần.
    painter.left(18)#Xoay Turtle sang trái 18 độ.
    drawsq(painter, 200)#Vẽ một hình vuông với độ dài cạnh là 200 pixel

turtle.done()#Giữ cửa sổ Turtle mở sau khi hoàn thành việc vẽ, để bạn có thể xem kết quả.
