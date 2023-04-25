from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")

N, M, K, X = map(int, s.readline().split())

road = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for i in range(M):
    A, B = map(int, s.readline().split())
    road[A].append(B)

distance = [0 for _ in range(N+1)]

def bfs(start):
    queue = deque([start])
    visited[start] = True
    
    while len(queue) != 0:
        now = queue.popleft()
        
        for next in road[now]:
            # 아직 방문하지 않았다면
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                distance[next] = distance[now] + 1

bfs(X)
result = []

for d in range(N+1):
    if distance[d] == K:
        result.append(d)
result.sort()
if len(result) == 0:
    print(-1)
else:
    for r in result:
        print(r)