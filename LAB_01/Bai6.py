s = input("Nhap chuoi: ")

hex_chars = "0123456789ABCDEFabcdef"
filtered = ""

for ch in s:
    if ch in hex_chars:
        filtered += ch

print("Chuoi Hex hop le sau khi loc:", filtered)

if filtered == "":
    print("Khong co ki tu Hex de doi.")
else:
    decimal = int(filtered, 16)
    print("Gia tri thap phan:", decimal)