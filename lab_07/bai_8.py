A = {1, 2.5, "abc", 3, "hello", 4.2}
count_int = 0
count_float = 0
count_str = 0

for x in A:
    if isinstance(x, int):
        count_int += 1
    elif isinstance(x, float):
        count_float += 1
    elif isinstance(x, str):
        count_str += 1
print("Số nguyên:", count_int)
print("Số thực:", count_float)
print("Chuỗi:", count_str)