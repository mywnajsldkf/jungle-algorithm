from sys import stdin as s
import sys

s = open("input.txt", "rt")

n = int(s.readline())
office = []
answer = [0 for i in range(n + 1)]

for i in range(n):
    t, p = map(int, s.readline().split())
    office.append([t, p])

print(office)

for i in range(n - 1, -1, -1):
    # 남은 t가 퇴사일 전보다 많다면
    if office[i][0] + i > n:
        answer[i] = answer[i+1]
    # 비교해서 업데이트한다.
    else:
        answer[i] = max(office[i][1] + answer[i + office[i][0]], answer[i+1])

print(answer[0])