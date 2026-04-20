ts = {}

n = int(input("Nhập số thí sinh: "))

for i in range(n):
    sbd = input("SBD: ")
    ten = input("Tên: ")
    diem = float(input("Điểm: "))
    
    ts[sbd] = {"ten": ten, "diem": diem}

# tra cứu
x = input("Nhập SBD cần tìm: ")

if x in ts:
    print(ts[x]["ten"], ts[x]["diem"])
else:
    print("Không có, nhập mới")
    ten = input("Tên: ")
    diem = float(input("Điểm: "))
    ts[x] = {"ten": ten, "diem": diem}

print(ts)