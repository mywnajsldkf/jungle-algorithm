import heapq

hq = []
print(hq)   # []

heapq.heappush(hq, 3)
heapq.heappush(hq, 2)
heapq.heappush(hq, 1)
print(hq)   # [1,3,2]   min Heap 기준으로 값 추가

# 값 삭제 후 반환한다.
print(heapq.heappop(hq))    # 1
print(heapq.heappop(hq))    # 2
print(heapq.heappop(hq))    # 3

# 기존 리스트를 Min Heap으로 변환한다.
hq = [3, 5, 4, 1, 2]
heapq.heapify(hq)
print(hq)       # [1, 2, 4, 5, 3]

# Max Heap 구현 방법 -> 추가 및 출력에 -를 붙인다.
heapq.heappush(hq, -1)
heapq.heappush(hq, -2)
heapq.heappush(hq, -3)

print(-heapq.heappop(hq))       # 3
print(-heapq.heappop(hq))       # 2
print(-heapq.heappop(hq))       # 1

hq = []
# Max Heap 구현 방법 -> 튜플을 이용한다.
heapq.heappush(hq, (-1, 1))
heapq.heappush(hq, (-2, 2))
heapq.heappush(hq, (-3, 3))

print(heapq.heappop(hq)[1])     # 3
print(heapq.heappop(hq)[1])     # 2
print(heapq.heappop(hq)[1])     # 1
