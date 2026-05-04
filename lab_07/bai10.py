m = input("Nhập m: ")
n = input("Nhập n: ")
chung = set(m) & set(n)
tong = 0
for x in chung:
    tong+=int(x)
print("Tổng chữ số chung:", tong)