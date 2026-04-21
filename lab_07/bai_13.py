W = input("Nhập chuỗi: ")
d = {}
for ch in W:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
print(d)