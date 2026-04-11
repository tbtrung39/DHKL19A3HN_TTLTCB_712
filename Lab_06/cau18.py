m = int(input("Số hàng: "))
n = int(input("Số cột: "))

ma_tran = []

for i in range(m):
    hang = list(map(int, input(f"Nhập hàng {i}: ").split()))
    ma_tran.append(hang)

tong = 0
for hang in ma_tran:
    tong += sum(hang)

print("Tổng:", tong)
