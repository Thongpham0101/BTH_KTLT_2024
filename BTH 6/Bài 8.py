class Bank:
    Account_type = "Savings"
    location = "Guntur"
    
    def __init__(self, name, Account_Number, balance):
        self.name = name
        self.Account_Number = Account_Number
        self.balance = balance
        self.Account_type = Bank.Account_type
        self.location = Bank.location

    def __repr__(self):
        print("Chào mừng bạn đến với Máy ATM PMT")
        print("--------------------------------")
        account_pin = int(input("Vui lòng nhập số pin của bạn: "))
        if account_pin == 123:
            Account(self)
        else:
            print("Pin không chính xác. Vui lòng thử lại")
            Error(self)
        return ' '.join([self.name, str(self.Account_Number)])

def Error(self):
    account_pin = int(input("Vui lòng nhập số pin của bạn: "))
    if account_pin == 123:
        Account(self)
    else:
        print("Số thẻ của bạn là: XXXX XXXX XXXX 1337")
        print("Bạn muốn gửi/rút tiền/Kiểm tra số dư?")
        print("""
1)             Balance
2)             Withdraw
3)             Deposit
4)             Quit
""")
        option = int(input("Vui lòng nhập lựa chọn của bạn: "))
        if option == 1:
            Balance(self)
        elif option == 2:
            Withdraw(self)
        elif option == 3:
            Deposit(self)
        elif option == 4:
            exit()

def Balance(self):
    print("Balance:", self.balance)
    Account(self)

def Withdraw(self):
    w = int(input("Vui lòng nhập số tiền mong muốn: "))
    if self.balance > 0 and self.balance >= w:
        self.balance -= w
        print("")
        print("Your Balance:", self.balance)
        print("")
    else:
        print("Giao dịch của bạn thành công")
        print("Số tiền trong tài khoản của bạn không đủ")
    Account(self)

def Deposit(self):
    d = int(input(": "))
    self.balance += d
    print("Giao dịch của bạn thành công")
    print("Balance:", self.balance)
    Account(self)

def Account(self):
    print("Account Menu")

def Exit():
    print("Exit")

# Tạo một đối tượng Bank với tên 'thongpham', số tài khoản 1453210145 và số dư 5000
t1 = Bank('thongpham', 1453210145, 5000)

# In đối tượng t1, sẽ gọi phương thức __repr__
print(t1)
