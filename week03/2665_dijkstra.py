from sys import stdin as s
import sys
import heapq

s = open("input.txt", "rt")

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

n = int(s.readline())

miro = []
for i in range(n):
    miro.append(list(map(int, s.readline().strip())))

visited = [[0 for _ in range(n)] for _ in range(n)]

def dijkstra(y, x):
    hq = []
    heapq.heappush(hq, (0, y, x))   # 비용, y좌표, x좌표
    visited[y][x] = 1

    while hq:
        cost, now_y, now_x = heapq.heappop(hq)
        if now_y == n-1 and now_x == n-1:
            return cost

        for d in range(4):
            new_y = now_y + dy[d]
            new_x = now_x + dx[d]
            if new_y < 0 or new_y >= n or new_x < 0 or new_x >= n:
                continue

            if visited[new_y][new_x] == 0:
                visited[new_y][new_x] = 1
                # 흰방을 만나면
                if miro[new_y][new_x] == 1:
                    heapq.heappush(hq, (cost, new_y, new_x))
                # 검은 방을 만나면, cost에 1 더한다.
                else:
                    heapq.heappush(hq, (cost+1, new_y, new_x))


print(dijkstra(0,0))