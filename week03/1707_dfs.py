import sys
sys.setrecursionlimit(10**6)
from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")

K = int(s.readline())


def dfs(start, group):
    visited[start] = group

    for i in graph[start]:
        if not visited[i]:
            a = dfs(i, -group)
            if not a:
                return False
        elif visited[i] == visited[start]:  # 현재와 연결된 정점의 그룹값이 같다면 -> 충돌난 것이니 False
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
            result = dfs(i, 1)
            if not result:      # False가 나왔다면 break
                break

    print("YES" if result else "NO")
