from sys import stdin as s
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
s = open("input.txt", "rt")

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, s.readline().split())
maze = []

for i in range(N):
    maze.append(list(map(int, s.readline().rstrip())))

count = 0
visited = [[False] * M for _ in range(N)]

queue = deque([[0, 0]])


def bfs():
    while len(queue) != 0:
        now = queue.popleft()
        for direction in range(4):
            new_y = now[0] + dy[direction]
            new_x = now[1] + dx[direction]
            # 범위 안에 있는지, 방문했는지 안했는지 확인
            if new_y < 0 or new_y >= N or new_x < 0 or new_x >= M:
                continue

            if visited[new_y][new_x]:
                continue

            if maze[new_y][new_x] != 1:
                continue

            queue.append([new_y, new_x])
            maze[new_y][new_x] = maze[now[0]][now[1]] + 1

    return maze[N-1][M-1]

print(bfs())
