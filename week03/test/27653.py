from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")

N = int(s.readline())
target = list(map(int, s.readline().split()))

tree = [[] for _ in range(N+1)]
checked = [False for _ in range(N+1)]

for i in range(N-1):
    u, v = map(int, s.readline().split())
    tree[u].append(v)
    tree[v].append(u)

# 연결되어있는 정점을 모두 확인한다.
def dfs(i)

for i in range(1, N+1):
    checked[i] = True   # 방문 표시한다. -> 해당 지점부터 탐색 시작
    bfs(i)