n = input("Nhập số: ")

i = 0
while i < len(n):
    ch = n[i]
    word = ""

    if ch == '0':
        word = "không"
    elif ch == '1':
        word = "một"
    elif ch == '2':
        word = "hai"
    elif ch == '3':
        word = "ba"
    elif ch == '4':
        word = "bốn"
    elif ch == '5':
        word = "năm"
    elif ch == '6':
        word = "sáu"
    elif ch == '7':
        word = "bảy"
    elif ch == '8':
        word = "tám"
    elif ch == '9':
        word = "chín"
    elif ch == '.':
        word = "phẩy"

    print(word, end=" ")
    i += 1