class Nguoi:
    def getGender(self):
        # Phương thức mặc định, trả về "Unknown"
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        # Ghi đè phương thức, trả về "Nam"
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        # Ghi đè phương thức, trả về "Nữ"
        return "Nữ"

# Tạo đối tượng của class Nam và Nu
aNam = Nam()
aNu = Nu()

# In ra giới tính
print(aNam.getGender())  # Kết quả: "Nam"
print(aNu.getGender())   # Kết quả: "Nữ"
