from sys import stdin as s
import sys

s = open("input.txt", "rt")

T = int(s.readline())

dp = [0] * 10001

for _ in range(T):
    N = int(s.readline())
    coins = list(map(int, s.readline().split()))

    M = int(s.readline())  # 동전으로 만들어야하는 금액

    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        dp[i][0] = 1

    for j in range(1, N + 1):
        for k in range(1, M + 1):
            dp[j][k] = dp[j - 1][k]
            if k - coins[j - 1] >= 0:
                dp[j][k] += dp[j][k - coins[j - 1]]

    print(dp[N][M])
