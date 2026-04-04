d = int(input("Nhap ngay: "))
m = int(input("Nhap thang: "))
y = int(input("Nhap nam: "))

# số ngày trong tháng
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    maxd = 31
elif m==4 or m==6 or m==9 or m==11:
    maxd = 30
else:
    maxd = 28

d = d + 1

if d > maxd:
    d = 1
    m = m + 1

if m > 12:
    m = 1
    y = y + 1

print(d, m, y)