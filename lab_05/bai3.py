
n = int(input("Nhập một số tự nhiên n: "))
n_ban_dau = n
if n == 0:
    chuoi_nhi_phan = "0"
else:
    chuoi_nhi_phan = ""  
    while n > 0:
        phan_du = n % 2  
        
        chuoi_nhi_phan = str(phan_du) + chuoi_nhi_phan 
        
        n = n // 2

print(f"Số {n_ban_dau} chuyển sang nhị phân là: {chuoi_nhi_phan}")