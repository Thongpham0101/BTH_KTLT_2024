import math

class Circle:
    def __init__(self, radius):
        # Khởi tạo bán kính
        self.radius = radius

    def area(self):
        # Tính diện tích: π * r^2
        return math.pi * (self.radius ** 2)

    def circumference(self):
        # Tính chu vi: 2 * π * r
        return 2 * math.pi * self.radius

# Sử dụng class
radius = 5  # Bán kính của hình tròn
circle = Circle(radius)

print(f"Bán kính: {radius}")
print(f"Diện tích: {circle.area():.2f}")
print(f"Chu vi: {circle.circumference():.2f}")
