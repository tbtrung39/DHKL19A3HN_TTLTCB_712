n = int(input("Nhập số SV: "))
sv = {}

for i in range(n):
    ma = input("Mã SV: ")
    ten = input("Tên: ")
    diem = int(input("Điểm (0-10): "))
    
    sv[ma] = {"ten": ten, "diem": diem}

# sắp xếp theo điểm giảm dần
sap_xep = sorted(sv.items(), key=lambda x: x[1]["diem"], reverse=True)

for ma, info in sap_xep:
    print(ma, info["ten"], info["diem"])