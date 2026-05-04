s = set()
print("Nhập ký tự (gõ 'ESC' để dừng):")
while True:
    ky_tu = input()
    if ky_tu == "ESC":
        break
    s.add(ky_tu)
so_moi = set()
for x in s:
    if not ('0' <= x <= '9'):
        so_moi.add(x)
print("Set sau khi xóa số:", so_moi)