n = int(input("Nhập n: "))

a = 0
b = 1

print(a, end=", ")
print(b, end=", ")

for i in range(2, n+1):
    c = a + b
    print(c, end=", ")
    a = b
    b = c