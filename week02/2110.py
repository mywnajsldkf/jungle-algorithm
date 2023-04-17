import sys
from sys import stdin as s

s = open("input.txt", "rt")

N, C = map(int, s.readline().split())

house = []
for i in range(N):
    house.append(int(s.readline()))

house.sort()

start = 1
end = house[-1] - house[0]

answer = 0

if C == 2:
    print(house[-1] - house[0])
else:
    while start <= end:
        middle = (start + end) // 2 # 공유기 사이의 거리 -> 몇 개의 공유기가 설치될 수 있는지 확인한다.
        current = house[0]
        count = 1

        for i in range(1, len(house)):
            if house[i] - middle >= current:
                count += 1
                current = house[i]

        # 공유기 숫자를 줄인다. -> 간격을 더 늘린다.
        if count >= C:
            start = middle + 1
            answer = middle
        # 공유기 숫자를 늘린다. -> 간격을 더 줄인다.
        else:
            end = middle - 1

    print(answer)