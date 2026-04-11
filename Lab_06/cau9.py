danh_sach = list(map(int, input("Nhập danh sách: ").split()))

for so in danh_sach:
    assert so % 2 == 0, "Có số không phải số chẵn!"

print("Tất cả đều là số chẵn")
