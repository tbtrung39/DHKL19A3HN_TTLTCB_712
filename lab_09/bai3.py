def tinh_luy_thua(co_so, so_mu):
    if so_mu == 0:
        return 1

    return co_so * tinh_luy_thua(co_so, so_mu - 1)

a = int(input("Nhập cơ số: "))
n = int(input("Nhập số mũ: "))
print("Kết quả:", tinh_luy_thua(a, n))