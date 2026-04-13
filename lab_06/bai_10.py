import random
a = []
for i in range(20):  # sinh 20 số
    while True:
        x = random.randint(0,200)
        if x % 5 == 0 and x % 7 == 0:
            a.append(x)
            break
print(a)