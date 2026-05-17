def solve(n, N, arr=[]):
    if n == 1:
        print(arr + [N])
        return

    for i in range(N + 1):
        solve(n - 1, N - i, arr + [i])

n = int(input("n = "))
N = int(input("N = "))
solve(n, N)