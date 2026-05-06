passwords = input("Nhập mật khẩu: ").split(",")
for p in passwords:
    if len(p) >= 6 and len(p) <= 12:
        co_thuong = False
        co_hoa = False
        co_so = False
        co_ky_tu = False

        for ch in p:
            if ch >= 'a' and ch <= 'z':
                co_thuong = True
            elif ch >= 'A' and ch <= 'Z':
                co_hoa = True
            elif ch >= '0' and ch <= '9':
                co_so = True
            elif ch in "$#@":
                co_ky_tu = True

        if co_thuong and co_hoa and co_so and co_ky_tu:
            print(p)