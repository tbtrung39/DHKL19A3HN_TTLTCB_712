n = int(input("Nhap so co 3 chu so: "))
tram = n // 100
chuc = (n // 10) % 10
don_vi = n % 10
doc = ["khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]
print("Cach doc:", doc[tram], "tram", doc[chuc], "muoi", doc[don_vi])