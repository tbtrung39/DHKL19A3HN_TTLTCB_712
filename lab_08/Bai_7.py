def find_min_max(a, b, c):
    return min(a, b, c), max(a, b, c)

a = int(input("Nhập số 1: "))
b = int(input("Nhập số 2: "))
c = int(input("Nhập số 3: "))

mn, mx = find_min_max(a, b, c)
print("Nhỏ nhất:", mn)
print("Lớn nhất:", mx)