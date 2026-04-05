s = input("Nhập chuỗi: ")
count = 0

for ch in s:
    if not ch.isalpha() and not ch.isdigit():
        count += 1

print("Số ký tự đặc biệt:", count)