a = float(input("Nhap a: "))
b = float(input("Nhap b: "))

def tinh_toan(a, b):
    print("Cong:", a + b)
    print("Tru:", a - b)
    print("Nhan:", a * b)
    if b != 0:
        print("Chia:", a / b)
    else:
        print("Khong chia duoc")

tinh_toan(a, b)