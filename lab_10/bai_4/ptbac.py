import math
def ptbac1(a,b):
    if a == 0:
        if b == 0:
            print('vo so no')
        else:
            print('vo no')
    else:
        x = -b / a
        print('nghiem x=', x)

def ptbac2(a,b,c):
    if a == 0:
        ptbac1(b,c)
    else:
        delta = b*b - 4*a*c
        if delta < 0:
            print('pt vo no')
        elif delta == 0:
            x = -b / (2*a)
            print('no kep x', x)
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)

            print('x1=', x1)
            print('x2=', x2)