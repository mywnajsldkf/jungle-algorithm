from sys import stdin as s
import sys
from collections import deque

s = open("input.txt", "rt")

n = int(s.readline())

# count, from(어떤 인덱스에서 왔는지)
dp = [[0, 0] for i in range(n+1)]

for i in range(2, n + 1):
    # f(x-1) + 1을 이용해서 DP 테이블을 채운다.
    dp[i][0] = dp[i - 1][0] + 1 # 직전 DP값에 +1
    dp[i][1] = i - 1            # 바로 앞에서 출발했으니까 인덱스를 바로 앞으로 업데이트

    # 2로 나누어 떨어지면, 2로 나누었을 때 몫 테이블의 dp에 +  1
    # dp를 업데이트했으므로 출발한 인덱스도 업데이트
    if i % 2 == 0:
        if dp[i][0] > dp[i // 2][0] + 1:
            dp[i][0] = dp[i // 2][0] + 1
            dp[i][1] = i // 2

    # 3으로 나누어 떨어지면, 3으로 나누었을 때 몫 테이블의 dp에 +  1
    # dp를 업데이트했으므로 출발한 인덱스도 업데이트
    if i % 3 == 0:
        if dp[i][0] > dp[i // 3][0] + 1:
            dp[i][0] = dp[i // 3][0] + 1
            dp[i][1] = i // 3
    print(dp)

print(dp[n][0])

loc = n
print(loc, end=' ')
# 출발한 시점부터 출력한다.
for i in range(dp[n][0]):
    print(dp[loc][1], end=' ')
    loc = dp[loc][1]