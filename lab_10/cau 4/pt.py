import math

def pt_bac_1(a, b):
    if a == 0:
        if b == 0:
            print("Vo so nghiem")
        else:
            print("Vo nghiem")
    else:
        x = -b / a
        print("Nghiem x =", x)

def pt_bac_2(a, b, c):
    if a == 0:
        pt_bac_1(b, c)

    else:
        delta = b * b - 4 * a * c

        if delta < 0:
            print("Vo nghiem")

        elif delta == 0:
            x = -b / (2 * a)
            print("Nghiem kep x =", x)

        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)

            print("x1 =", x1)
            print("x2 =", x2)