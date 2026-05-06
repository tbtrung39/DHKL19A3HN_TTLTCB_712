str = input("Nhập chuỗi: ").upper()
hex_chars = "0123456789ABCDEF"

hop_le = True
for ch in str:
    if ch not in hex_chars:
        hop_le = False
        break

if hop_le:
    print("Chuỗi là hệ Hex")
else:
    moi = ""
    for ch in str:
        if ch in hex_chars:
            moi += ch

    print("Chuỗi sau khi lọc:", moi)

    if moi != "":
        print("Số thập phân:", int(moi, 16))