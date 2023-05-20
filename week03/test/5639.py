from sys import stdin as s
from collections import deque
s = open("input.txt", "rt")

T = int(s.readline())

dy = [0,-1,0,1]
dx = [1,0,-1,0]

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = True

    while queue:
        now_y, now_x = queue.popleft()
        for i in range(4):
            new_y = now_y + dy[i]
            new_x = now_x + dx[i]

            if new_y < 0 or new_y >= N or new_x < 0 or new_x >= M:
                continue

            if visited[new_y][new_x]:
                continue

            if bat[new_y][new_x] == 1:
                visited[new_y][new_x] = True
                queue.append((new_y, new_x))


for i in range(T):
    count = 0
    M, N, K = map(int, s.readline().split())
    bat = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    for _k in range(K):
        x, y = map(int, s.readline().split())
        bat[y][x] = 1

    for _i in range(N):
        for _j in range(M):
            # 배추가 심어져 있고, 이전에 방문한 적이 없다면
            if bat[_i][_j] == 1 and not visited[_i][_j]:
                count += 1
                bfs(_i,_j)

    print(count)