Str = input('Nhập vào một chuỗi ký tự: ')
print('Ký tự của bạn nhập là:', Str)
dem = 0
for i in Str:
    if "0" <= i <= "9":
        dem += 1
print('Số các ký tự là số trong chuỗi ký tự bạn vừa nhập là:',dem)