from sys import stdin as s
import sys
from collections import deque

s = open("input.txt", "rt")

n = int(s.readline())
dp = [0] * (n + 1)

for i in range(2, n+1):
    # 이전 것에서 이어서 온다고 가정한다.
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])