import re
ten_dang_nhap = input("Nhập tên đăng nhập: ")
mat_khau = input("Nhập mật khẩu: ")
hop_le = (
    6 <= len(mat_khau) <= 12 and
    re.search("[a-z]", mat_khau) and
    re.search("[A-Z]", mat_khau) and
    re.search("[0-9]", mat_khau) and
    re.search("[$#@]", mat_khau)
)
if hop_le:
    print("Mật khẩu hợp lệ")
else:
    print("Mật khẩu không hợp lệ")