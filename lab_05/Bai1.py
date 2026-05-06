str = input("Nhập chuỗi: ")
dem = 0

for ch in str:
    if ch.isdigit():
        dem += 1

print("Số ký tự là số:", dem)