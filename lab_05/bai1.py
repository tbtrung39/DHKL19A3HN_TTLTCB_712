chuoi = input("Nhập chuỗi: ")
dem = 0
for ky_tu in chuoi:
    if '0' <= ky_tu <= '9':
        dem += 1
print("Số ký tự là số:", dem)