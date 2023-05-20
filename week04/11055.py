from sys import stdin as s
import sys

s = open("input.txt", "rt")

n = int(s.readline())
a = list(map(int, s.readline().split()))

# dp = [0] * n
dp = [1]*n
dp[0] = a[0]

# print(a)

# 시작점
for i in range(1, n):
    # 0부터 시작하면서,
    # 시작점보다 큰 것을 확인하면 시작점이 크다면 해당 dp에 시작점+1과 dp[i]를 비교하여 큰 것을 업데이트한다
    for j in range(i):
        print(i, j)
        # 더 작은 것을 만나면, 비교하여 추가해주고
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + a[i])
        # 더 큰 것을 만나면 dp를 업데이트해준다.
        else:
            dp[i] = max(dp[i], a[i])

print(dp)
# print(max(dp))