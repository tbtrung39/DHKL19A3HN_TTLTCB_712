chuoi = input("Nhập chuỗi: ").upper()
chuoi_hex = ""
for ky_tu in chuoi:
    if ('0' <= ky_tu <= '9') or ('A' <= ky_tu <= 'F'):
        chuoi_hex += ky_tu
if chuoi_hex == chuoi:
    print("Chuỗi là hệ Hex hợp lệ")
else:
    print("Chuỗi không phải hệ Hex, sau khi lọc còn:", chuoi_hex)
if chuoi_hex == "":
    print("Không có giá trị để chuyển")
else:
    so_thap_phan = int(chuoi_hex, 16)
    print("Giá trị thập phân:", so_thap_phan)