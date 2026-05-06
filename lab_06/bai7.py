List_ = [["mon",73],["tue",89],["wed",95],
         ["thu",103],["fri",115],["sat",128],["sun",120]]

for i in List_:
    print(i)
print(List_[2][1])

List_.append(["new", 100])

tong = 0
tong = tong + List_[1][1]
tong = tong + List_[2][1]
tong = tong + List_[5][1]
tong = tong + List_[6][1]

print("Tổng:", tong)