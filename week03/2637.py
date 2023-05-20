from sys import stdin as s
import sys
from collections import deque

sys.setrecursionlimit(10**6)
s = open("input.txt", "rt")

n = int(s.readline())
m = int(s.readline())

graph = [[] for _ in range(n+1)]
need = [[0] * (n+1) for _ in range(n+1)]    # 기본 부품의 수

queue = deque()
degree = [0] * (n+1)

for i in range(m):
    x, y, k = map(int, s.readline().split())
    graph[y].append((x, k))
    degree[x] += 1  # y다음에 필요한 것, 차수가 큰 것이 뒤에 오는 것

for i in range(1, n+1):
    if degree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()

    for next, next_need in graph[now]:
        if need[now].count(0) == n + 1:
            need[next][now] += next_need
        else:
            for i in range(1, n+1):
                need[next][i] += need[now][i] * next_need

        degree[next] -= 1
        if degree[next] == 0:
            queue.append(next)

# 가장 마지막 번
for i in range(len(need[n])):
    if need[n][i] > 0:
        print(i, need[n][i])

'''
for x in enumerate(needs[n]):
    if x[1] > 0:
        print(*x)
'''
