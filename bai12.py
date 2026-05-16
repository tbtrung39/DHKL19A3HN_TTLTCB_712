# Bài 12: Bài toán gà chó bằng đệ quy

def gacho(ga, cho):
    if ga + cho == 36 and 2 * ga + 4 * cho == 100:
        print("Ga =", ga)
        print("Cho =", cho)
        return

    if ga > 36:
        return

    gacho(ga + 1, 36 - (ga + 1))

gacho(0, 36)