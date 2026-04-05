Str = input("Nhập vào một chuỗi (Str): ")
ky_tu_hex_hop_le = "0123456789abcdefABCDEF"

chuoi_hex = ""

for ky_tu in Str:
    if ky_tu in ky_tu_hex_hop_le:
        chuoi_hex += ky_tu

if len(chuoi_hex) == len(Str):
    print("-> Đây là một chuỗi chuẩn hệ Hex.")
else:
    print("-> Chuỗi này chứa ký tự không thuộc hệ Hex.")
    print("-> Chuỗi sau khi đã loại bỏ các ký tự sai là:", chuoi_hex)

if chuoi_hex != "":
    so_thap_phan = int(chuoi_hex, 16) 
    print("-> Giá trị ở hệ thập phân là:", so_thap_phan)
else:
    print("-> Không có ký tự Hex nào trong chuỗi để chuyển đổi!")