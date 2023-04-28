from sys import stdin as s
import sys

s = open("input.txt", "rt")

n = int(s.readline())
dp = [0] * (n+2)

dp[1] = 1
dp[2] = 2


def tile(n):
    if n == 1:
        return dp[1]
    elif n == 2:
        return dp[2]
    else:
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) % 15746
        return dp[n]

print(tile(n))