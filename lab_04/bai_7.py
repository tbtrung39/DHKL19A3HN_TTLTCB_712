a = int(input("a: "))
b = int(input("b: "))
i = max(a, b)
while True:
    if i % a == 0 and i % b == 0:
        print("BCNN:", i)
        break
    i += 1