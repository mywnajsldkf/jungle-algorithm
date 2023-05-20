from sys import stdin as s
import sys
from collections import deque

s = open("input.txt", "rt")

n = int(s.readline())

# 나이 순서대로 정렬한 것을 적당히 나누는 방식!!!!
grade = [0]
grade.extend(list(map(int, s.readline().split())))

dp = [0 for _ in range(n + 1)]

dp[0] = 0

if n >= 2:
    dp[2] = max(grade[2], grade[1]) - min(grade[2], grade[1])

print(dp)

for i in range(3, len(grade) + 1):
    dp[i] = max(dp[i-1], max(grade[i], grade[i-1]) - min(grade[i], grade[i-1]), )
