chuoi = input("Nhập chuỗi: ")
chuoi_so = ""
for ky_tu in chuoi:
    if '0' <= ky_tu <= '9':
        chuoi_so += ky_tu

print("Chuỗi số sau khi lọc:", chuoi_so)
if chuoi_so == "":
    print("Không có số để kiểm tra")
else:
    n = int(chuoi_so)
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    if tong == n and n != 0:
        print(n, "là số hoàn hảo")
    else:
        print(n, "không phải số hoàn hảo")