# Bài 1: Tìm số lớn nhất trong 3 số bằng đệ quy

def max3(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))

print("So lon nhat:", max3(a, b, c))