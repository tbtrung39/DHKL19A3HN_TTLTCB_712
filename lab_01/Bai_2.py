s = int(input("Nhap giay: "))

d = s // (24*3600)
s = s % (24*3600)

h = s // 3600
s = s % 3600

m = s // 60
s = s % 60

print(d, "ngay", h, "gio", m, "phut", s, "giay")