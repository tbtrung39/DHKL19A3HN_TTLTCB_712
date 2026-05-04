m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
A = []
for i in range(m):
    hang = list(map(int, input("Nhập hàng: ").split()))
    A.append(hang)
print("Ma trận A:")
for hang in A:
    print(hang)

#b
tong = 0
for hang in A:
    for x in hang:
        tong += x
print("Tổng các phần tử:", tong)