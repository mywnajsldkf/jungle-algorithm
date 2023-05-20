from sys import stdin as s
import sys
from collections import deque

s = open("input.txt", "rt")

N, M = map(int, s.readline().split())
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)    # 차수 저장

queue = deque()
answer = []


for i in range(M):
    a, b = map(int, s.readline().rstrip().split())
    graph[a].append(b)
    degree[b] += 1      # 차수를 늘려서 뒤로 빌어낸다.

# 차수가 0인 것(앞에 와야하는 것, 정확한 순서가 중요한 것이 아니다.)이 앞에 온다. -> 출발지점을 앞으로
for i in range(1, N+1):
    if degree[i] == 0:
        queue.append(i)


# 출발지점을 정답 지점에 하나씩 넣고, 출발지점과 연결된 노드들 중에 위치를 하나씩 배면서 채운다.
while queue:
    tmp = queue.popleft()
    answer.append(tmp)
    for i in graph[tmp]:
        degree[i] -= 1
        if degree[i] == 0:
            queue.append(i)

print(*answer)