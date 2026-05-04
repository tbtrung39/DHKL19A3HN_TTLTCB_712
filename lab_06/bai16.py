X = int(input("Nhập X: "))
Y = int(input("Nhập Y: "))
mang = []
for i in range(X):
    hang = []
    for j in range(Y):
        hang.append(i * j)
    mang.append(hang)

print("Mảng 2 chiều:")
print(mang)