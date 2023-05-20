import sys
from sys import stdin as s

s = open("input.txt", "rt")

def getArea(histogram, n):
    stack = []
    maxArea = 0

    for i in range(n):
        '''
        이전 막대보다 현재 히스토그램 높이가 작으면
        자신보다 작거나 같은 것들은 모두 pop하여 최대 넓이는 구한다.
        '''
        while (len(stack) != 0 and histogram[stack[-1]] > histogram[i]):
            height = histogram[stack.pop()]  # 이전 체인의 높이

            # pop하고 이전 체인이 없어 비어있다면 0번째 index부터 (i-1)번째 인덱스까지 유일한 폭이 된다.
            if len(stack) == 0:
                width = i
            # 비어있지 않다면, 더 작은 높이를 가진 체인이 있다는 것이다.
            else:
                width = i - 1 - stack[-1]

            maxArea = max(maxArea, height * width)  # 최대 넓이 갱신

        '''
        i보다 작거나 같은 것이므로 넣어준다.
        '''
        stack.append(i)

    while len(stack) != 0:
        height = histogram[stack.pop()]

        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1] - 1
        maxArea = max(maxArea, width * height)

    return maxArea


while True:
    case = list(map(int, s.readline().split()))
    n = case.pop(0)

    if n == 0:
        break

    print(getArea(case, n))