r = float(input("Nhập bán kính r: "))
h = float(input("Nhập chiều cao h: "))
pi = 3.14
s_xq = 2 * pi * r * h
s_tp = s_xq + 2 * pi * (r**2)
the_tich = pi * (r**2) * h
print("Diện tích xung quanh là:", round(s_xq, 2))
print("Diện tích toàn phần là:", round(s_tp, 2))
print("Thể tích khối trụ là:", round(the_tich, 2))