from heapq import heappop, heappush
from sys import stdin as s

s = open("input.txt", "rt")

# 백준이가 외치는 정수의 개수
N = int(s.readline())

# 오름차순으로 정렬
leftHeap = []
# 내림차순으로 정렬
rightHeap = []

for i in range(N):
    number = int(s.readline())

    # leftHeap과 rightHeap에 번갈아 넣어주면서 균형을 맞춘다.
    if len(leftHeap) == len(rightHeap):
        heappush(leftHeap, -number)     # 최대힙으로 구성 -> 오름차순
    else:
        heappush(rightHeap, number)     # 최소힙으로 구성 -> 내림차순

    # rightHeap 원소가 있을 때
    # 각자의 맨 뒤에 꺼내온 것
    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftValue = heappop(leftHeap)
        rightValue = heappop(rightHeap)

        # 값 비교 후 교체하여 왼쪽은 중간값보다 작은 값, 오른쪽은 중간값보다 큰 값이 들어가도록 한다.
        heappush(leftHeap, -rightValue)
        heappush(rightHeap, -leftValue)

    print(-leftHeap[0])