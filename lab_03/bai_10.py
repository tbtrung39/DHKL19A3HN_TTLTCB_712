n = int(input("Nhập n: "))

for i in range(2, n+1):
    dem = 0
    
    for j in range(1, n+1):
        if n % i == 0:
            n = n // i
            dem += 1
    
    if dem > 0:
        print(i, "^", dem)