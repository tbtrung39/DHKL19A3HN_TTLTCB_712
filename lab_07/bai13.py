W = input("Nhap chuoi W: ")
K = input("Nhap chuoi K: ")
dem = 0
len_W = len(W)
len_K = len(K)
for i in range(len_W - len_K + 1):
    if W[i:i+len_K] == K:
        dem += 1

d = {K: dem}
print(d)