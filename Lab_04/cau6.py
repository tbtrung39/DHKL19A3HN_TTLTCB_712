chuoi_so = input("Nhập một số: ")

ket_qua = ""  
i = 0        
while i < len(chuoi_so):
    so_hien_tai = chuoi_so[i]
    if so_hien_tai == '0':
        ket_qua += "không "
    elif so_hien_tai == '1':
        ket_qua += "một "
    elif so_hien_tai == '2':
        ket_qua += "hai "
    elif so_hien_tai == '3':
        ket_qua += "ba "
    elif so_hien_tai == '4':
        ket_qua += "bốn "
    elif so_hien_tai == '5':
        ket_qua += "năm "
    elif so_hien_tai == '6':
        ket_qua += "sáu "
    elif so_hien_tai == '7':
        ket_qua += "bảy "
    elif so_hien_tai == '8':
        ket_qua += "tám "
    elif so_hien_tai == '9':
        ket_qua += "chín "
    i += 1 
print("Kết quả in ra màn hình là:", ket_qua)