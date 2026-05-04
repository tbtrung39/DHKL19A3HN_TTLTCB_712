lst = list(map(int, input("Nhập list: ").split()))
for x in lst:
    assert x % 2 == 0, "Có số không phải số chẵn!"
print("Tất cả đều là số chẵn")