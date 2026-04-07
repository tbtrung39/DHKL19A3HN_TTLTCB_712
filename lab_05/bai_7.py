s = input("Nhập chuỗi: ")
num_str = ""
for ch in s:
    if ch.isdigit():
        num_str += ch
print("Chuỗi số:", num_str)

if num_str != "":
    n = int(num_str)
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i

    if tong == n:
        print("Là số hoàn hảo")
    else:
        print("Không phải số hoàn hảo")