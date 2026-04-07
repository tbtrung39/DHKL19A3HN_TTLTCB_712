s = input("Nhập chuỗi: ")
words = s.replace(",", " ").split()
for w in words:
    print(w)