n = int(input("Nhập số nguyên dương: "))

print("Phân tích:", n, "=")

i = 2
while n > 1:
    if n % i == 0:
        print(i, end=" ")
        n = n // i
    else:
        i += 1