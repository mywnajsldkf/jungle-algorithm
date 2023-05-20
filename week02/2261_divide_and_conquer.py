import sys
import math
from sys import stdin as s

s = open("input.txt", "rt")

N = int(s.readline())
dots = []
for i in range(N):
    dot = list(map(int, s.readline().split()))
    dots.append(dot)

dots.sort()

def dist(point1, point2):
    return (point2[1]-point1[1]) ** 2 + (point2[0] - point1[0]) ** 2

def getMidDistance(start, mid, end, minDistance):
    searchList = []         # 탐색할 좌표 리스트
    midX = dots[mid][0]     # mid의 x 좌표

    for i in range(start, end+1):
        # minDistance가 제곱값이므로 xDistance도 제곱으로 계산한다.
        xDistance = (dots[i][0] - midX) ** 2    # x 좌표 차이

        # 탐색하면서 추가로 확인할 곳을 집어넣음
        if (xDistance < minDistance):
            searchList.append(dots[i])

    # y축을 기준으로 정렬한다.
    searchList.sort(key = lambda x : x[1])

    # 후보군들을 순회하면서 y좌표 차이가 minDist내에 있는 원소들만 거리 측정한다.
    for i in range(len(searchList)-1):
        for j in range(i+1, len(searchList)):
            # i번째 점과 j번째 점을 비교하여 y좌표거리를 측정한다.
            # 측정된 y좌표가 minDist보다 작으면, i,j 점의 거리를 측정하여 minDist와 측정한 거리 중 작은 값으로 갱신한다.
            yDist = searchList[i][1] - searchList[j][1]
            if math.pow(yDist, 2) < minDistance:
                minDistance = min(dist(searchList[i], searchList[j]), minDistance)
            else:
                break
    return minDistance

# 3개 중에 가장 가까운 거리를 구한다. -> n^2 방식
def bruteDistance(left, right):
    distance = sys.maxsize
    for i in range(left, right):
        for j in range(i+1, right+1):
            temp = dist(dots[j], dots[i])
            distance = min(temp, distance)

    return distance

def findClosestPair(left, right):
    # 3개 중에 가장 가까운 거리를 구한다.
    if (right - left) < 3:
        distance = bruteDistance(left, right)
        return distance

    # 가운데 위치를 구한다.
    mid = (left + right) // 2

    # 위치 기준으로 나눠서 leftDistance와 rightDistance를 구한다.
    leftDistance = findClosestPair(left, mid)
    rightDistance = findClosestPair(mid + 1, right)

    # 더 짧은 길이를 저장한다.
    minDistance = min(leftDistance, rightDistance)

    minDistance = min(minDistance, getMidDistance(left, mid, right, minDistance))

    return minDistance

print(int(findClosestPair(0, len(dots)-1)))