t = float(input("Thoi gian (giay): "))

P = 220 * 2.7  # công suất (W)
kwh = (P * t) / (1000 * 3600)

tien = kwh * 7000
print(round(tien, 2))
