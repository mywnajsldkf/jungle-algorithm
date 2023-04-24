from sys import stdin as s
import sys
from collections import deque
sys.setrecursionlimit(10**9)
s = open("input.txt", "rt")

n = int(s.readline())
m = int(s.readline())

computer = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, s.readline().split())
    computer[a].append(b)
    computer[b].append(a)

visited = [False for i in range(n+1)]


def bfs(start):
    count = 0
    queue = deque([start])

    visited[start] = True

    while len(queue) != 0:
        now = queue.popleft()
        for i in computer[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1

    return count

print(bfs(1))