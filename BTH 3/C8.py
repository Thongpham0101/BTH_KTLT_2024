import math;
x,y=0,0
moves=["up 5","down 3", "left 3","right 2"]
for moves in moves:
    direction, steps = moves.split()
    steps= int(steps)
    if direction=="up":
        y+=steps
    elif direction=="down":
        y-=steps
    elif direction=="left":
        x-=steps
    elif direction=="right":
        x+=steps
distance=math.sqrt(x**2 + y**2)
print("Khoảng cách từ vị trí ban đầu đến điểm hiện tại là: ", round(distance))
print("PHẠM MẠNH THỐNG")
print("MSV:235752021610071")
