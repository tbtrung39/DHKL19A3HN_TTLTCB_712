so_n = int(input("Nhập n: "))

day_fibo = [0, 1]

for i in range(2, so_n):
    day_fibo.append(day_fibo[i-1] + day_fibo[i-2])

print(", ".join(map(str, day_fibo[:so_n])))

