s1 = input("Chuỗi 1: ")
s2 = input("Chuỗi 2: ")

m, n = len(s1), len(s2)
dp = [[""]*(n+1) for _ in range(m+1)]

for i in range(m):
    for j in range(n):
        if s1[i] == s2[j]:
            dp[i+1][j+1] = dp[i][j] + s1[i]
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], key=len)

print("Chuỗi chung dài nhất:", dp[m][n])