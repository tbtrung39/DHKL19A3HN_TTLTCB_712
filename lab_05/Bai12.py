str1 = input("Nhập chuỗi: ")

# thay dấu phẩy bằng khoảng trắng
str1 = str1.replace(",", " ")

ds = str1.split()

for word in ds:
    print(word)