from heapq import heappop, heappush
from sys import stdin as s

s = open("input.txt", "rt")

N = int(s.readline())
heap = []
result = 0

for i in range(N):
    number = int(s.readline())
    heappush(heap, number)

if N == 1:
    print(0)
else:
    while len(heap) > 1:
        # result와 이전 것을 꺼내서 다시 더한다.
        add = heappop(heap) + heappop(heap) # 더한 것을 가지고 이어서 또 계산하기 때문
        result += add
        heappush(heap, add)
    print(result)