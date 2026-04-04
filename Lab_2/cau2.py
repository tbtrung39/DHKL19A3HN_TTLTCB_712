a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Vô số nghiệm")
        else:
            print("Vô nghiệm")
    else:
        print("Nghiệm:", -c/b)
else:
    delta = b*b - 4*a*c
    
    if delta < 0:
        print("Vô nghiệm")
    elif delta == 0:
        print("Nghiệm kép:", -b/(2*a))
    else:
        x1 = (-b + delta**0.5)/(2*a)
        x2 = (-b - delta**0.5)/(2*a)
        print("x1 =", x1)
        print("x2 =", x2)