tn = int(input())  # tháng
luong_cb = 1350000

if tn < 12:
    hs = 2.34
elif tn < 36:
    hs = 3.33
elif tn < 60:
    hs = 3.66
else:
    hs = 3.99

print(hs * luong_cb)