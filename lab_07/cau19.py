nv = {}

while True:
    print("\n1. Thêm")
    print("2. Tìm")
    print("3. Tăng lương")
    print("4. Xóa")
    print("5. Sắp xếp")
    print("0. Thoát")

    chon = input("Chọn: ")

    if chon == "1":
        ma = input("Mã NV: ")
        ten = input("Tên: ")
        ns = int(input("Năm sinh: "))
        luong = int(input("Lương: "))
        nv[ma] = {"ten": ten, "ns": ns, "luong": luong}

    elif chon == "2":
        x = input("Nhập mã: ")
        if x in nv:
            print(nv[x])
        else:
            print("Không có")

    elif chon == "3":
        y = input("Mã cần tăng lương: ")
        if y in nv:
            nv[y]["luong"] += 1000000

    elif chon == "4":
        z = input("Mã cần xóa: ")
        if z in nv:
            del nv[z]

    elif chon == "5":
        sap_xep = sorted(nv.items(), key=lambda x: x[1]["ns"], reverse=True)
        for ma, info in sap_xep:
            print(ma, info)

    elif chon == "0":
        break