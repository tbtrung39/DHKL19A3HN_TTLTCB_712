x = float(input("Nhap x: "))

f = (-x + (x*x + 4)**0.5) / ((x**4 + 1)**(1/3))

print(round(f, 2))