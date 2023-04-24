from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")

N, M, V = map(int, s.readline().split())

array = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]


for i in range(M):
    a, b = map(int, s.readline().split())
    array[a].append(b)
    array[b].append(a)
bfs_result = []
dfs_result = []

for i in array:
    i.sort()


def bfs(start):
    nodes = deque([start])
    visited[start] = True

    while len(nodes) != 0:
        now = nodes.popleft()
        bfs_result.append(now)
        for i in array[now]:
            if not visited[i]:
                nodes.append(i)
                visited[i] = True


def dfs(start):
    visited[start] = True
    dfs_result.append(start)

    for i in array[start]:
        if not visited[i]:
            dfs(i)

dfs(V)
visited = [False for _ in range(N + 1)]
bfs(V)

for i in dfs_result:
    print(i, end=' ')
print()
for i in bfs_result:
    print(i, end=' ')
