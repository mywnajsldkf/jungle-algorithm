from sys import stdin as s
from collections import deque

import sys
sys.setrecursionlimit(10**9)
s = open("input.txt", "rt")

M, N, H = map(int, s.readline().split())

dz = [0, -1, 0, 0, 1, 0]
dy = [0, 0, 1, 0, 0, -1]
dx = [1, 0, 0, -1, 0, 0]

tomato = [[[] for _j in range(N)] for _k in range(H)]
visited = [[[False for _i in range(M)] for _j in range(N)] for _k in range(H)]

days = 0
'''
이렇게 보면 층같이 보인다.
for i in tomato:
    print(i)
'''

for _i in range(H):
    for _j in range(N):
        tomato[_i][_j] = list(map(int, s.readline().split()))
# print(tomato)
queue = deque([])

for _i in range(H):
    for _j in range(N):
        for _k in range(M):
            if tomato[_i][_j][_k] == 1:
                queue.append([_i, _j, _k])

while len(queue) != 0:
    now = queue.popleft()
    visited[now[0]][now[1]][now[2]] = True
    for i in range(6):
        new_z = now[0] + dz[i]
        new_y = now[1] + dy[i]
        new_x = now[2] + dx[i]

        # 범위 확인
        if new_z < 0 or new_z >= H or new_y < 0 or new_y >= N or new_x < 0 or new_x >= M:
            continue

        # 방문 확인
        if not visited[new_z][new_y][new_x] and tomato[new_z][new_y][new_x] == 0:
            queue.append([new_z, new_y, new_x])
            tomato[new_z][new_y][new_x] = tomato[now[0]][now[1]][now[2]] + 1

for _i in range(H):
    for _j in range(N):
        for _k in range(M):
            if tomato[_i][_j][_k] == 0:
                print(-1)
                exit(0)
            else:
                days = max(days, tomato[_i][_j][_k])

print(days-1)