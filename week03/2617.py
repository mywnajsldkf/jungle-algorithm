from sys import stdin as s
import sys
from collections import deque
sys.setrecursionlimit(10**6)
s = open("input.txt", "rt")

n = int(s.readline())
m = int(s.readline())

computer = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, s.readline().split())
    computer[a].append(b)
    computer[b].append(a)

visited = [False for i in range(n+1)]

count = 0
def dfs(start):
    global count
    count += 1
    visited[start] = True

    for i in computer[start]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(count-1)