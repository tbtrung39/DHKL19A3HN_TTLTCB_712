A = list(map(int, input("Nhập list: ").split()))
ok = True
for x in A:
    if x % 2 != 0:
        ok = False
if ok:
    print("Tất cả đều chẵn")
else:
    print("Có số lẻ")