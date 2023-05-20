import sys
from sys import stdin as s

s = open("input.txt", "rt")

N = int(s.readline())

dot = []

for i in range(N):
    dot.append(list(map(int, s.readline().split())))

dot.sort()

start = dot[0][0]
end = dot[0][1]

length = 0

for i in range(1, len(dot)):
    x = dot[i][0]
    y = dot[i][1]
    print("start:", start, "end:", end)

    # 끝이 연장되는 경우
    if x <= end and y > end:
        end = y

    # 포함되는 경우
    elif x <= end and y <= end:
        continue

    # 새롭게 시작하는 경우
    elif x > end:
        # 계산한다.
        print(start, end)
        length += (end - start)

        start = x
        end = y

length += (end - start)
print(length)