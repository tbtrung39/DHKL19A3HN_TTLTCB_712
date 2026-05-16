def tim(ga):

    if ga > 36:
        return

    cho = 36 - ga

    if ga * 2 + cho * 4 == 100:
        print("So ga =", ga)
        print("So cho =", cho)
        return

    tim(ga + 1)


tim(0)