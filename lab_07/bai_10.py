m = input("Nhập m: ")
n = input("Nhập n: ")

set_m = set(m)
set_n = set(n)

common = set_m & set_n
print("Chữ số chung:", common)

total = 0
for x in common:
    total += int(x)
print("Tổng:", total)