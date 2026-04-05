x = float(input("Nhập góc x: "))
cos_x = 1          
hang_hien_tai = 1  
lan_lap = 1        
while abs(hang_hien_tai) > 1e-4:
    hang_hien_tai = -hang_hien_tai * x * x / ((2*lan_lap-1)*(2*lan_lap))
    cos_x += hang_hien_tai
    lan_lap += 1
print("cos(x) ≈", cos_x)