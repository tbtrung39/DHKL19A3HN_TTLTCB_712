import random
List = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("Danh sách:", List)
print("Phần tử cần chọn:", List[1][1])
print("Độ dài:", len(List))
List.append(["rand", random.randint(50, 150)])
print("Sau khi thêm:", List)
tong = List[1][1] + List[2][1] + List[5][1] + List[6][1]
print("Tổng:", tong)