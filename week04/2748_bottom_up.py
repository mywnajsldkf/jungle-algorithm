from sys import stdin as s
import sys

s = open("input.txt", "rt")

n = int(s.readline())

dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])