import my_triange
a = float(input('nhap canh a:'))
b = float(input('nhap canh b:'))
c = float(input('nhap canh c:'))

if my_triange.is_TamGiac(a,b,c):
    print('day la tam giac')
    print('chu vi', my_triange.chuviTamGiac(a,b,c))
    print('dien tich', my_triange.S_TamGiac(a,b,c))
else:
    print('khong phai tam giac')