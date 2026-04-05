chuoi = input("Nhập chuỗi: ").upper()

ky_tu_hex = "0123456789ABCDEF"
chuoi_hop_le = ""

# lọc ký tự hợp lệ
for ky_tu in chuoi:
    if ky_tu in ky_tu_hex:
        chuoi_hop_le += ky_tu

print("Chuỗi sau khi lọc:", chuoi_hop_le)

# chuyển sang thập phân
so_thap_phan = 0

for ky_tu in chuoi_hop_le:
    so_thap_phan = so_thap_phan * 16 + int(ky_tu, 16)

print("Số thập phân:", so_thap_phan)