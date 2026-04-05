Str1 = input("Nhập chuỗi thứ nhất: ")
Str2 = input("Nhập chuỗi thứ hai: ")

if len(Str1) > len(Str2):
    Str1, Str2 = Str2, Str1 

chuoi_chung_max = ""

do_dai_str1 = len(Str1)
for do_dai in range(do_dai_str1, 0, -1):
    
    for i in range(do_dai_str1 - do_dai + 1):
        chuoi_con = Str1[i : i + do_dai]
        
        if chuoi_con in Str2:
            chuoi_chung_max = chuoi_con
            break  
            
    if chuoi_chung_max != "":
        break

if chuoi_chung_max == "":
    print("Hai chuỗi không có ký tự nào chung!")
else:
    print(f"Chuỗi con chung dài nhất là: '{chuoi_chung_max}'")