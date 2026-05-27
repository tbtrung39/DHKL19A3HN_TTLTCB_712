from doicoso import doicoso1
from doicoso import doicoso2


# Bai 5
n = int(input("Nhap so nguyen: "))

print("He 2 =", doicoso1.nhi_phan(n))
print("He 8 =", doicoso1.bat_phan(n))
print("He 16 =", doicoso1.thap_luc_phan(n))


# Bai 6
s = input("Nhap chuoi: ")

chuoi_moi = doicoso2.loc_ky_tu(s)

print("Chuoi sau khi loc =", chuoi_moi)

print("He so =", doicoso2.he_so(chuoi_moi))

print("1010 sang he 10 =",
      doicoso2.he2_sang10("1010"))

print("17 sang he 10 =",
      doicoso2.he8_sang10("17"))

print("1A sang he 10 =",
      doicoso2.he16_sang10("1A"))