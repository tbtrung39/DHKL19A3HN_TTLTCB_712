danh_sach = [
    ["mon", 73], ["tue", 89], ["wed", 95],
    ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]
]
for phan_tu in danh_sach:
    print(phan_tu)
print("Giá trị cần lấy:", danh_sach[1][1])
print("Độ dài:", len(danh_sach))
tong = danh_sach[1][1] + danh_sach[2][1] + danh_sach[5][1] + danh_sach[6][1]
print("Tổng:", tong)
