def tinh_toan(a, b):
    print("Cộng:", a + b)
    print("Trừ:", a - b)
    print("Nhân:", a * b)
    if b != 0:
        print("Chia:", a / b)
    else:
        print("Không chia được cho 0")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
tinh_toan(a, b)