# Bài 3: Tính a^n bằng đệ quy

def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)

a = int(input("Nhap a: "))
n = int(input("Nhap n: "))

print("Ket qua:", power(a, n))