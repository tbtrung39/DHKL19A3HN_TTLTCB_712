str = input("Nhập chuỗi: ")
dem = 0

for ch in str:
    if not ch.isalpha() and not ch.isdigit():
        dem += 1

print("Số ký tự đặc biệt:", dem)