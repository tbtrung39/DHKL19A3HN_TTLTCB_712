n = input("Nhập số: ")
i = 0
while i < len(n):
    ch = n[i]
    if ch == '0':
        print("không", end=" ")
    elif ch == '1':
        print("một", end=" ")
    elif ch == '2':
        print("hai", end=" ")
    elif ch == '3':
        print("ba", end=" ")
    elif ch == '4':
        print("bốn", end=" ")
    elif ch == '5':
        print("năm", end=" ")
    elif ch == '6':
        print("sáu", end=" ")
    elif ch == '7':
        print("bảy", end=" ")
    elif ch == '8':
        print("tám", end=" ")
    elif ch == '9':
        print("chín", end=" ")

    i += 1