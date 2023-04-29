from sys import stdin as s
import sys

s = open("input.txt", "rt")

T = int(s.readline())

dp = [0] * 10001

for _ in range(T):
    N = int(s.readline())
    coins = list(map(int, s.readline().split()))
    M = int(s.readline())  # 동전으로 만들어야하는 금액

    dp = [0] * (M + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(1, M+1):
            if i >= coin:
                dp[i] += dp[i-coin]

    print(dp[M])