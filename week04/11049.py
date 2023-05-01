from sys import stdin as s
import sys

s = open("input.txt", "rt")

n = int(s.readline())

matrix = [list(map(int, s.readline().split())) for i in range(n)]
dp = [[0] * n for i in range(n)]    # 행렬이 하나라면 비용이 0이다.

for cnt in range(n-1):
    for i in range(n-1-cnt):
        j = i + cnt + 1

        dp[i][j] = 2**31    # 가장 큰 수로 업데이트
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0]*matrix[k][1]*matrix[j][1])

print(dp[0][-1])