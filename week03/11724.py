from sys import stdin as s
from collections import deque

import sys
sys.setrecursionlimit(10**6)

s = open("input.txt", "rt")

N, M = map(int, s.readline().split())

connection = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, s.readline().split())
    connection[u].append(v)
    connection[v].append(u)

visited = [False for i in range(N+1)]

def dfs(start):

    for i in connection[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)