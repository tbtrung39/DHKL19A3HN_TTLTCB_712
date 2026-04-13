a = []
while True:
    x = int(input("nhập:"))
    if x == 0:
        break
    a.append(x)

b = [1, 2, 3]

a = b + a
a = a + b
if len(a) >= 4:
    a[4:4] = b
else:
    print("Danh sách chưa đủ 5 phần tử để chèn")
print("Sau khi chèn:", a)
# xóa phần tử k
k = int(input("Nhập k: "))
if 0 <= k < len(a):
    del a[k]
else:
    print("k không hợp lệ")
print("Sau khi xóa:", a)
#sắp xếp danh sách tăng dần và giảm dần
a.sort()
print("Tăng dần:", a)

a.sort(reverse=True)
print("Giảm dần:", a)