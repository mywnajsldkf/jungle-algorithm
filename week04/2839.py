from sys import stdin as s
import sys

s = open("input.txt", "rt")

n = int(s.readline())

# 어디서 왔는지
# 3kg, 5kg

dp = [[0 for _ in range(n+1)] for _ in range(2)]
dp[1][0] = 1
for i in range(1, n+1):
    if i < 3:
        dp[1][i] = 0
    elif 3 <= i < 5:
        dp[1][i] = dp[1][i-3]
        dp[0][i] = i - 3
    elif i >= 5:
        a = dp[1][i-3]
        b = dp[1][i-5]

        if b == 1:
            dp[1][i] = 1
            dp[0][i] = i - 5
        elif a == 1:
            dp[1][i] = 1
            dp[0][i] = i - 3

if dp[1][n] == 0:
    print(-1)
else:
    count = 1
    now = dp[0][n]

    while now != 0:
        count += 1
        now = dp[0][now]

    print(count)