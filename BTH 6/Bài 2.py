class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
        # Khởi tạo chiều dài và chiều rộng
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def dien_tich(self):
        # Tính diện tích hình chữ nhật
        return self.chieu_dai * self.chieu_rong

# Tạo một đối tượng của class Hinhchunhat với chiều dài và chiều rộng
hcn = Hinhchunhat(5, 3)

# In diện tích của hình chữ nhật
print("Diện tích hình chữ nhật:", hcn.dien_tich())
