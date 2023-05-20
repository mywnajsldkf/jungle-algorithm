from sys import stdin as s
import sys
from collections import deque

s = open("input.txt", "rt")

n = int(s.readline())
miro = list(map(int, s.readline().split()))

visited = [-1 for _ in range(n)]


def isPossible(dx):
    # 범위 밖이면 갈 수 없다.
    if dx > n:
        return False

    # 0이라면 방문하지 않는다.
    if miro[dx] == 0:
        return False

    # 방문하지 않았다면
    if visited[dx] == -1:
        return True

def bfs(start, target):
    queue = deque()
    queue.append(start)
    visited[start] = 0

    while queue:
        now = queue.popleft()
        distance = [_ for _ in range(1, miro[now] + 1)]
        for x in distance:
            new_x = now + x
            # 도착 지점이라면
            if new_x == target:
                return
            if isPossible(new_x):
                queue.append(new_x)
                visited[new_x] = visited[now] + 1


bfs(0, n)
print(visited[n-1])