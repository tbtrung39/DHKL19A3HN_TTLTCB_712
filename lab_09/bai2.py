def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)

n = int(input("Nhập số lượng phần tử: "))
ds = []
for i in range(n):
    x = int(input("nhap số phần tử:"))
    ds.append(x)
kq = ds[0]
for i in range(1, n):
    kq = ucln(kq, ds[i])
print("UCLN là:", kq)