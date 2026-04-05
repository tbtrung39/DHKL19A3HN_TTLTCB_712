a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

i = 1
while True:
    if i % a == 0 and i % b == 0:
        print("BCNN =", i)
        break
    i += 1