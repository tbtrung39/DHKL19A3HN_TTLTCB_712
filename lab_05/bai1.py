s = input("Nhập chuỗi: ")
dem = 0
for c in s:
    if c >= '0' and c <= '9':
        dem += 1
print("Số ký tự là số:", dem)