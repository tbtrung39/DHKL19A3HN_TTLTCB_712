import doicoso2

s = input("Nhap chuoi: ")

chuoi_moi = doicoso2.loc_ky_tu(s)

print("Chuoi sau khi loc =", chuoi_moi)

print("He so cua chuoi =", doicoso2.he_so(chuoi_moi))

print("1010 tu he 2 sang he 10 =",
      doicoso2.he2_sang10("1010"))

print("17 tu he 8 sang he 10 =",
      doicoso2.he8_sang10("17"))

print("1A tu he 16 sang he 10 =",
      doicoso2.he16_sang10("1A"))