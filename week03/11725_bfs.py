from sys import stdin as s
from collections import deque

import sys

sys.setrecursionlimit(10 ** 6)

s = open("input.txt", "rt")

N = int(s.readline())

tree = [[] for i in range(N + 1)]

for i in range(N - 1):
    start, end = map(int, s.readline().split())
    tree[start].append(end)
    tree[end].append(start)

result = [0] * (N - 1)
visited = [False] * (N + 1)

def bfs(start):
    queue = deque([start])

    while len(queue) != 0:
        now = queue.popleft()
        visited[now] = True
        for i in tree[now]:
            if not visited[i]:
                result[i-2] = now
                queue.append(i)

for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)

for i in result:
    print(i)
