from sys import stdin as s
from collections import deque
s = open("input.txt", "rt")

dx = [-1, 1]

N, K = map(int, s.readline().split())

max_range = max(N, K)

visited = [-1 for _ in range(max_range * 2 + 1)]

def isPossible(x):
    # 범위 확인
    if x < 0 or x >= max_range * 2 + 1:
        return False

    # 이전에 방문하지 않았다면
    if visited[x] == -1:
        return True

def bfs(start, end):
    queue = deque()
    #  bfs 할 곳) 저장
    queue.append((1, start))
    visited[start] = None

    while queue:
        now_count, now_x = queue.popleft()
        # now_parent = now[0]
        # now_x = now[1]

        # 목표 점 도달
        if now_x == end:
            # print(visited[end]-1)
            print(now_count-1)
            print(visited)

            result = []
            path_index = end
            for i in range(now_count):
                result.append(path_index)
                path_index = visited[path_index]

            result.reverse()
            for i in result:
                print(i, end=" ")
            break

        for i in [now_x + 1, now_x - 1, now_x * 2]:
            next_x = i

            if isPossible(next_x):
                queue.append((now_count + 1, next_x))
                visited[next_x] = now_x

bfs(N, K)

