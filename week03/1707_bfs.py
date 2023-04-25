from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")

K = int(s.readline())

def bfs(start, group):
    queue = deque([start])
    visited[start] = group

    while len(queue) != 0:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = -1 * visited[now]
            elif visited[i] == visited[now]:
                return False
    return True


for t in range(K):
    V, E = map(int, s.readline().split())
    graph = [[] for i in range(V+1)]        # 빈 그래프 생성
    visited = [False for i in range(V+1)]   # 방문한 정점 확인

    for i in range(E):
        start, end = map(int, s.readline().split())
        graph[start].append(end)
        graph[end].append(start)

    for i in range(1, V+1):
        if not visited[i]:
            result = bfs(i, 1)
            if not result:
                break

    print("YES" if result else "NO")