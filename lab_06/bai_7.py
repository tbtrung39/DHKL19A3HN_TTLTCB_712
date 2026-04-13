import random
List_ = [["mon",73], ["tue",89], ["wed",95], ["thu",103], ["fri",115], ["sat",128], ["sun",120]]
# in danh sách
for x in List_:
    print(x)
#phần tử thứ 2, vị trí thứ 3
print(List_[1][1])
# kiểm tra độ dài
if len(List_) > 0:
    print("Độ dài list:", len(List_))
# tạo sublist ngẫu nhiên
    ngay = random.choice(["mon","tue","wed","thu","fri","sat","sun"])
    value = random.randint(50,150)
    sub = [ngay, value]
# thêm vào list
    List_.append(sub)
    print("Sau khi thêm:", List_)
else:
    print("List rỗng")
# tổng sale thứ 2,3,7,cn
tong = 0
for i in [1,2,5,6]:
    tong += List_[i][1]
print("Tổng =", tong)