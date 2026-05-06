def ngto(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Nhập n: "))
if ngto(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không phải là số nguyên tố")
print("Các số nguyên tố nhỏ hơn", n, "là:")
for i in range(2, n):
    if ngto(i):
        print(i, end=" ")