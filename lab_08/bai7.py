def so_nho_nhat(a, b, c):
    return min(a, b, c)

def so_lon_nhat(a, b, c):
    return max(a, b, c)

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

print("Số nhỏ nhất:", so_nho_nhat(a, b, c))
print("Số lớn nhất:", so_lon_nhat(a, b, c))