
Str = input("Nhập vào một chuỗi ký tự: ")
dem = 0
for ky_tu in Str:
    if not (('a' <= ky_tu <= 'z') or ('A' <= ky_tu <= 'Z') or ('0' <= ky_tu <= '9')):
        dem += 1 
print("Số lượng ký tự không phải chữ cái tiếng Anh và không phải số là:", dem)