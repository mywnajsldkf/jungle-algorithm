from sys import stdin as s
import sys

s = open("input.txt", "rt")

n = int(s.readline())

arr = list(map(int, s.readline().split()))
dp = arr

def findMaxSum():
    for i in range(1, len(dp)):
        dp[i] = max(dp[i-1] + arr[i], dp[i])
findMaxSum()

print(max(dp))