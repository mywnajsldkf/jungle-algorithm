import sys
from sys import stdin as s
from collections import deque
s = open("input.txt", "rt")

dy = [1, 0, -1, -1, -1, 0, 1, 1]
dx = [1, 1, 1, 0, -1, -1, -1, 0]

N, M = map(int, s.readline().split())

sea = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]


for i in range(N):
    sea[i] = list(map(int, s.readline().split()))


def bfs(count, queue):
    while queue:
        now_y, now_x = queue.popleft()
        visited[now_y][now_x] = True

        # 동서 남북 대각선 확인하기
        for i in range(8):
            new_y = now_y + dy[i]
            new_x = now_x + dx[i]

            if new_y < 0 or new_y >= N or new_x < 0 or new_x >= M:
                continue

            if not visited[new_y][new_x] and sea[new_y][new_x] == 0:
                sea[new_y][new_x] = count
                visited[new_y][new_x] = True


count = 1
while True:

    zero_count = 0
    count += 1

    queue = deque()

    for i in range(N):
        for j in range(M):
            # 방문하지 않았고, 상어가 있다.
            if sea[i][j] == 0:
                zero_count += 1
            else:
                queue.append((i, j))

    if zero_count == 0:
        break
    else:
        bfs(count, queue)

print(count-2)