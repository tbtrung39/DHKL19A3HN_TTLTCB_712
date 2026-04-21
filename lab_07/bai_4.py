chieucao = [161,182,161,154,176,170,167,171,170,174,150,142,148,165,170,178,156,145,149,163,
162,159,165,165,170,180,155,159,155,153,152,162,180,168,169,168,167,170]
# a
print("Số sinh viên:", len(chieucao))
# b
avg = sum(chieucao) / len(chieucao)
print("Chiều cao trung bình:", round(avg, 2))
# c
chieucaokhacnhau = set(chieucao)
print("Các chiều cao khác nhau:", chieucaokhacnhau)