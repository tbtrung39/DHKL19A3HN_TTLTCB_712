str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")

m = len(str1)
n = len(str2)

dp = [[0]*(n+1) for _ in range(m+1)]
max_len = 0
end_pos = 0

for i in range(1, m+1):
    for j in range(1, n+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            if dp[i][j] > max_len:
                max_len = dp[i][j]
                end_pos = i

kq = str1[end_pos-max_len:end_pos]
print("Chuỗi con chung dài nhất:", kq)