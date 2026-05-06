def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

tu = int(input("Nhập tử: "))
mau = int(input("Nhập mẫu: "))
ucln = gcd(tu, mau)
print("Phân số rút gọn:", tu // ucln, "/", mau // ucln)