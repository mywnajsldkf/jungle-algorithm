from sys import stdin as s
from collections import deque
s = open("input.txt", "rt")

dx = [-1, 1]

N, K = map(int, s.readline().split())

max_range = max(N, K)

visited = [False for _ in range(max_range * 2 + 1)]

def isPossible(x):
    # 범위 확인
    if x < 0 or x >= max_range * 2 + 1:
        return False

    # 이전에 방문하지 않았다면
    if not visited[x]:
        return True

def bfs(start, end):
    queue = deque()
    queue.append([[], start])
    visited[start] = 1

    while queue:
        now = queue.popleft()
        now_parent = now[0]
        now_x = now[1]

        # 목표 점 도달
        if now_x == end:
            print(visited[end]-1)

            for i in now_parent:
                print(i, end=' ')
            print(now_x)
            break

        for i in range(2):
            next_x = now_x + dx[i]
            # 방문할 수 있다면
            if isPossible(next_x):

                next_parent = []
                for i in now_parent:
                    next_parent.append(i)

                next_parent.append(now_x)
                queue.append([next_parent, next_x])
                visited[next_x] = visited[now_x] + 1

        next_x = now_x * 2
        if isPossible(next_x):

            next_parent = []
            for i in now_parent:
                next_parent.append(i)
            next_parent.append(now_x)
            queue.append([next_parent, next_x])
            visited[next_x] = visited[now_x] + 1


bfs(N, K)