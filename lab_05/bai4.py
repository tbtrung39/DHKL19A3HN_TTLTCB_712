
Str1 = input("Nhập chuỗi thứ nhất (Str1): ")
Str2 = input("Nhập chuỗi thứ hai (Str2): ")
ket_qua = ""

do_dai_max = max(len(Str1), len(Str2))

for i in range(do_dai_max):
    if i < len(Str1):
        ket_qua += Str1[i]
        
    if i < len(Str2):
        ket_qua += Str2[i]

print("Chuỗi sau khi trộn là:", ket_qua)