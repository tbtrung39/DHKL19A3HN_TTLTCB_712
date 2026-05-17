def tim_ga_cho(tong_con, tong_chan):

    for ga in range(tong_con + 1):

        cho = tong_con - ga

        so_chan = ga * 2 + cho * 4

        if so_chan == tong_chan:
            print("Số gà là:", ga)
            print("Số chó là:", cho)

tong_con = 36
tong_chan = 100
tim_ga_cho(tong_con, tong_chan)