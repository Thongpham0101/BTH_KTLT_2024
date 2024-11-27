class Circle:
    def __init__(self, r):
        # Gán bán kính r vào thuộc tính radius của đối tượng
        self.radius = r

    def area(self):
        # Tính diện tích của hình tròn
        return self.radius ** 2 * 3.14

# Tạo một đối tượng của class Circle với bán kính là 2
aCircle = Circle(2)

# In ra diện tích của hình tròn
print(aCircle.area())
