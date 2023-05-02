from sys import stdin as s
import sys
from collections import deque

s = open("input.txt", "rt")

n, k = map(int, s.readline().split())

max_range = max(n, k)

visited = [-1 for _ in range(max_range * 2 + 1)]


def is_possible(x):
    if x < 0 or x >= max_range * 2 + 1:
        return False
    if visited[x] == -1:
        return True


def bfs(start, end):
    queue = deque()
    queue.append((1, start))
    visited[start] = None

    while queue:
        now_count, now_x = queue.popleft()

        if now_x == end:
            print(now_count - 1)
            result = []
            path_index = end

            for i in range(now_count):
                result.append(path_index)
                path_index = visited[path_index]

            result.reverse()
            print(*result)
            break

        for next in [now_x - 1, now_x + 1, now_x * 2]:
            if is_possible(next):
                queue.append((now_count + 1, next))
                visited[next] = now_x


bfs(n, k)