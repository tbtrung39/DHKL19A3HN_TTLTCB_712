m = input("Nhập m: ")
n = input("Nhập n: ")

set_m = set(m)
set_n = set(n)

chung = set_m & set_n

tong = 0
for x in chung:
    tong += int(x)

print("Các chữ số chung:", chung)
print("Tổng:", tong)