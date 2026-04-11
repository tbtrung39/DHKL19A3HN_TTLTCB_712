import re

chuoi = input("Nhập mật khẩu: ")
danh_sach = chuoi.split(",")

hop_le = []

for mat_khau in danh_sach:
    if (6 <= len(mat_khau) <= 12 and
        re.search("[a-z]", mat_khau) and
        re.search("[A-Z]", mat_khau) and
        re.search("[0-9]", mat_khau) and
        re.search("[$#@]", mat_khau)):
        hop_le.append(mat_khau)

print(",".join(hop_le))
