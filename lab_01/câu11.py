import math
a = float(input("Nhập vận tốc a: "))
t = (a**4) / math.log(5, 4)
print("Thời gian ô tô đi được đến lúc dừng là:", round(t, 2))