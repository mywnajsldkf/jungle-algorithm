from sys import stdin as s
import sys

s = open("input.txt", "rt")

n = int(s.readline())

dp = [0] * (n + 1)

if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    dp[1] = 1
    dp[2] = 1

    if n >= 3:
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])