import sys
from sys import stdin as s

s = open("input.txt", "rt")

def getMidArea(low, high, mid):
    toLeft = mid
    toRight = mid

    height = histogram[mid]  # 높이를 구한다.

    maxArea = height  # 폭이 1이므로 넓이가 높이 = 면적이 된다.

    # toLeft는 low 밖이 영역 밖이므로
    # toRight는 right 안으로
    while low < toLeft and high > toRight:
        # 높은 값을 선택한다.
        # height는 기존보다 작거나 같에 갱신한다.

        # 오른쪽이 더 크므로 오른쪽으로 이동한다.
        if histogram[toLeft - 1] < histogram[toRight + 1]:
            toRight += 1
            height = min(height, histogram[toRight])
        # 왼쪽이 더 크므로 왼쪽으로 이동한다.
        else:
            toLeft -= 1
            height = min(height, histogram[toLeft])

        maxArea = max(maxArea, height * (toRight - toLeft + 1))

    # 왼쪽 구간을 탐색하지 못한 경우
    while low < toLeft:
        toLeft -= 1
        height = min(height, histogram[toLeft])
        maxArea = max(maxArea, height * (toRight - toLeft + 1))

    # 오른쪽 구간을 다 탐색하지 못한 경우
    while high > toRight:
        toRight += 1
        height = min(height, histogram[toRight])
        maxArea = max(maxArea, height * (toRight - toLeft + 1))

    return maxArea


def getArea(low, high):
    # 막대 폭(넓이)이 1일 경우, 높이가 넓이가 된다.
    if low == high:
        return histogram[low]

    # 1. 가운데 위치를 구한다.
    mid = (low + high) // 2

    # 2. 가운데 위치 기준으로 나눠서 큰 것을 저장한다.
    leftArea = getArea(low, mid)
    rightArea = getArea(mid + 1, high)

    # 3. leftArea와 rightArea 중 큰 것을 구한다.
    maxArea = max(leftArea, rightArea)

    # 4. 구간의 최대 넓이를 구한다.
    maxArea = max(getMidArea(low, high, mid), maxArea)

    return maxArea


while True:
    histogram = list(map(int, s.readline().split()))
    if histogram[0] == 0:
        break

    n = histogram.pop(0)

    print(getArea(0, len(histogram) - 1))