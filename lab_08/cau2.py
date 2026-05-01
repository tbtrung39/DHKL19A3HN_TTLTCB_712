def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def rut_gon(tu, mau):
    g = ucln(tu, mau)
    return tu // g, mau // g

tu = int(input("Tu: "))
mau = int(input("Mau: "))
t, m = rut_gon(tu, mau)
print("Phan so:", t, "/", m)