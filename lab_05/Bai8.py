str = input("Nhập đoạn văn: ")
tu = input("Nhập từ cần tìm: ")

ds = str.split()
dem = 0

for w in ds:
    if w == tu:
        dem += 1

print("Số lần xuất hiện:", dem)