Str1 = "Khoa, khoa học ung dung"

Str1_da_sua = Str1.replace(",", " ")

danh_sach_tu = Str1_da_sua.split()

print("Các từ trong chuỗi là:")
for tu in danh_sach_tu:
    print(tu)