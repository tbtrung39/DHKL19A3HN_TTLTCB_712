s = input("Nhập chuỗi: ")
dem = 0
for c in s:
    if not (('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')):
        dem += 1
print("Số ký tự đặc biệt:", dem)