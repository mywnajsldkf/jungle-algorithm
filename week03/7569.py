import sys
from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")

M, N, H = list(map(int, s.readline().split()))

arr = [[list(map(int, s.readline().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False] * M for _ in range(N)] for _ in range(H)]

queue = deque()

dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, -1, 1]

def bfs():

    while queue:
        z, y, x = queue.popleft()

        for i in range(6):
            new_z = z + dz[i]
            new_y = y + dy[i]
            new_x = x + dx[i]

            if new_z < 0 or new_z >= H or new_y < 0 or new_y >= N or new_x < 0 or new_x >= M:
                continue

            # 값이 0이고 방문하지 않았다면 -> 이후에 방문한다.
            if arr[new_z][new_y][new_x] == 0 and not visited[new_z][new_y][new_x]:
                queue.append((new_z, new_y, new_x))
                arr[new_z][new_y][new_x] = arr[z][y][x] + 1
                visited[new_z][new_y][new_x] = True


for _i in range(H):
    for _j in range(N):
        for _k in range(M):
            if arr[_i][_j][_k] == 1 and not visited[_i][_j][_k]:
                queue.append((_i, _j, _k))
                visited[_i][_j][_k] = True

bfs()

max_count = -sys.maxsize

for i in arr:
    for j in i:
        max_count = max(max_count, max(j))
        for k in j:
            if k == 0:
                print(-1)
                sys.exit()


print(max_count - 1)