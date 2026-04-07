s = input("Nhập chuỗi: ").upper()
hex_chars = "0123456789ABCDEF"
valid = True

for ch in s:
    if ch not in hex_chars:
        valid = False
        break

if valid:
    print("Hợp lệ HEX:", int(s, 16))
else:
    new_s = ""
    for ch in s:
        if ch in hex_chars:
            new_s += ch
    print("Chuỗi hợp lệ:", new_s)
    print("Đổi sang thập phân:", int(new_s, 16))