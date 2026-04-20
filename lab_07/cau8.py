A = {1, 2.5, "abc", 3, 4.7, "hello", 10}

dem_int = 0
dem_float = 0
dem_str = 0

for x in A:
    if type(x) == int:
        dem_int += 1
    elif type(x) == float:
        dem_float += 1
    elif type(x) == str:
        dem_str += 1

print("Số nguyên:", dem_int)
print("Số thực:", dem_float)
print("Chuỗi:", dem_str)