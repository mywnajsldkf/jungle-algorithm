from sys import stdin as s
import sys

s = open("input.txt", "rt")

n = int(s.readline())
a = list(map(int, s.readline().split()))

dp = [1] * n

print(a)

# 시작점
for i in range(1, n):
    # 0부터 시작하면서,
    # 시작점보다 큰 것을 확인하면 시작점이 크다면 해당 dp에 시작점+1과 dp[i]를 비교하여 큰 것을 업데이트한다.
    for j in range(i-1, -1, -1):
        print(i, j)
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))