str = input("Nhập chuỗi: ")

so = ""
for ch in str:
    if ch.isdigit():
        so += ch

print("Chuỗi số:", so)

if so != "":
    n = int(so)
    tong = 0

    for i in range(1, n):
        if n % i == 0:
            tong += i

    if tong == n:
        print("Là số hoàn hảo")
    else:
        print("Không phải số hoàn hảo")
else:
    print("Không có số")