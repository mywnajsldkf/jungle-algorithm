from heapq import heappop, heappush
from sys import stdin as s
import heapq

s = open("input.txt", "rt")

N = int(s.readline())
location = []
roads = []

for i in range(N):
    location.append(list(map(int, s.readline().split())))

d = int(s.readline())

for road in location:
    h, o = road
    if abs(h - o) <= d:
        roads.append(sorted(road))

# 철로의 시작점을 가장 작은 것부터 시작하기 위해 큰 원소 기준으로 오름차순한다.
roads.sort(key=lambda x: x[1])

answer = 0
heap = []

for road in roads:
    # heap에 없으면 추가하고
    if not heap:
        heapq.heappush(heap, road)
    else:
        # heap[0][0]: 가장 맨 위에 있는 위치 정보의 시작 점
        # road[1]: 끝 점
        while heap[0][0] < road[1] - d:
            heapq.heappop(heap) # 가장 작은 것이 빠져 나온다.
            if not heap:        # 더 이상 조회할 정보가 없으므로 pop
                break
        heapq.heappush(heap, road)
    answer = max(answer, len(heap))

print(answer)