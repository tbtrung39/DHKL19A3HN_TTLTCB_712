thu = int(input("Nhập thứ (1-7): "))
if thu < 1 or thu > 7:
    print("yeu cau nhap lai!")
else:
    if thu == 1:
            print("Monday")
    elif thu == 2:
        print("Tuesday")
    elif thu == 3:
        print("Wednesday")
    elif thu == 4:
        print("Thursday")
    elif thu == 5:
        print("Friday")
    elif thu == 6:
        print("Saturday")
    else:
        print("Sunday")