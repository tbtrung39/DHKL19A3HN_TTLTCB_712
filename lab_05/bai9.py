
Str = input("Nhập vào một chuỗi ký tự: ")

if len(Str) == 0:
    print("Chuỗi rỗng!")
else:
    chuoi_max = Str[0]
    chuoi_hien_tai = Str[0]

    for i in range(1, len(Str)):
        if Str[i] == Str[i-1]:
            chuoi_hien_tai += Str[i] 
        else:
            if len(chuoi_hien_tai) > len(chuoi_max):
                chuoi_max = chuoi_hien_tai  
            
            chuoi_hien_tai = Str[i]

    if len(chuoi_hien_tai) > len(chuoi_max):
        chuoi_max = chuoi_hien_tai

    print("Chuỗi ký tự con giống nhau dài nhất là:", chuoi_max)