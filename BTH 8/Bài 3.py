import turtle
import random

colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow","black"]

painter = turtle.Turtle()
painter.pensize(3)

for i in range(11)#Vòng lặp này sẽ chạy 11 lần.
    color = random.choice(colors)
    painter.pencolor(color)
    painter.circle(100)
    painter.right(30) # Đảm bảo rằng tổng góc xoay trong 1 vòng lặp không vượt quá 360 độ
    # Không cần thiết phải thêm painter.left(60)
    painter.setposition(0, 0)

turtle.done()
