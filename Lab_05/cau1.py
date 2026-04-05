s = input("Nhập chuỗi: ")
count = 0

for ch in s:
    if ch.isdigit():
        count += 1

print("Số ký tự là số:", count)