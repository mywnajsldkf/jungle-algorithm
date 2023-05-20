from sys import stdin as s
import sys

s = open("input.txt", "rt")

t = int(s.readline())


def sticker(n):
    if n == 1:
        return max(dp[0][0], dp[1][0])

    if n == 2:
        dp[0][1] = dp[1][0] + arr[0][1]
        dp[1][1] = dp[0][0] + arr[1][1]

        return max((dp[0][0] + arr[1][1]), (dp[1][0] + arr[0][1]))

    else:
        dp[0][1] = dp[1][0] + arr[0][1]
        dp[1][1] = dp[0][0] + arr[1][1]

        for i in range(2, n):
            dp[0][i] = max(dp[1][i - 1] + arr[0][i], max(dp[0][i - 2], dp[1][i - 2]) + arr[0][i])
            dp[1][i] = max(dp[0][i - 1] + arr[1][i], max(dp[1][i - 2], dp[0][i - 2]) + arr[1][i])


for i in range(t):
    n = int(s.readline())

    arr = [list(map(int, s.readline().split())), list(map(int, s.readline().split()))]
    dp = arr

    # print(dp)

    sticker(n)

    print(max(dp[1][n - 1], dp[0][n - 1]))