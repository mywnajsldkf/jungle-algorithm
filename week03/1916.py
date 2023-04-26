import heapq
from sys import stdin as s

s = open("input.txt", "rt")
INF = int(1e9)          # 무한

N = int(s.readline())
M = int(s.readline())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    start, end, cost = map(int, s.readline().split())   # 출발, 도착, 비용
    graph[start].append((end, cost))

start_city, end_city = map(int, s.readline().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거치면 이동 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start_city)

print(distance[end_city])