def sv(g,c):
    if g + c == 36 and 2*g + 4*c == 100:
        print('gà =', g)
        print('chó =', c)
        return
    sv(g+1, c-1)
sv(0,36)