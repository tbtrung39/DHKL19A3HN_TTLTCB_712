a = float(input())
b = float(input())
c = float(input())

d = b*b - 4*a*c

if d < 0:
    print("Vo nghiem")
elif d == 0:
    x = -b / (2*a)
    print(round(x,2))
else:
    x1 = (-b + d**0.5) / (2*a)
    x2 = (-b - d**0.5) / (2*a)
    print(round(x1,2), round(x2,2))
    