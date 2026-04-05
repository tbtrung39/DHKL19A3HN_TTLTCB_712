Str = """Lòng tôi tan nát khi nhận ra tôi là gay"""

tu_can_tim = input("Nhập từ đơn cần tìm: ")

Str_thuong = Str.lower()
tu_can_tim = tu_can_tim.lower()

danh_sach_dau_cau = [".", ",", "!", "?", "\n"]
for dau in danh_sach_dau_cau:
    Str_thuong = Str_thuong.replace(dau, " ")

danh_sach_cac_tu = Str_thuong.split()

dem = 0
for tu in danh_sach_cac_tu:
    if tu == tu_can_tim:  
        dem += 1

print(f"-> Từ '{tu_can_tim}' xuất hiện {dem} lần trong đoạn văn bản.")