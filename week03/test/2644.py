from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")

n = int(s.readline())
a, b = map(int, s.readline().split())
m = int(s.readline())

family = [[] for i in range(n+1)]

for i in range(m):
    x, y = map(int, s.readline().split())
    family[x].append(y)
    family[y].append(x)

visited = [False for i in range(n+1)]

def bfs(start, target):
    queue = deque([start])
    visited[start] = True
    is_success = False

    while len(queue) != 0:
        now = queue.popleft()
        # 찾았다.
        if now == target:
            is_success = True
            break
        else:
            for next in family[now]:
                if visited[next] == False:
                    queue.append(next)
                    visited[next] = visited[now] + 1

    if is_success:
        print(visited[now]-1)
    else:
        print(-1)

bfs(a, b)