from sys import stdin as s
from collections import deque
# import sys

# sys.setrecursionlimit(10**6)
s = open("input.txt", "rt")

N, M = map(int, s.readline().split())

ice = [[] * M for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

print(*visited, sep='\n')

for i in range(N):
    ice[i] = list(map(int, s.readline().split()))


def bfs(y, x):


def isDivided():
    count = 0
    queue = deque()
    for i in range(N):
        for j in range(M):
            if ice[i][j] != 0:
                count += 1
                queue.append((i, j))
                bfs(i, j)

count = 0
while True:
    # 빙산 덩어리의 개수를 확인한다.
    if not isDivided():
        count += 1
        # bfs(queue, count)
