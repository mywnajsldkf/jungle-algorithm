import sys
from sys import stdin as s

s = open("input.txt", "rt")
M, N, L = map(int, s.readline().split()) # 사대의 수, 동물의 수, 사정거리
shooting = list(map(int, s.readline().split()))
shooting.sort()

animal = []
count = 0

for i in range(N):
    animal.append(list(map(int, s.readline().split())))

def findPosition(numbers, key):
    left = 0
    right = M-1

    while left <= right:
        middle = (left + right) // 2

        if key == numbers[middle]:
            return numbers[middle]
            break
        elif key < numbers[middle]:
            right = middle - 1
        elif key > numbers[middle]:
            left = middle + 1

    if right == -1:
        return numbers[0]
    elif left == M:
        return numbers[M-1]
    else:
        prev_num = numbers[left-1]
        next_num = numbers[right+1]

        prev_step = abs(key - prev_num)
        next_step = abs(key - next_num)

        if prev_step == next_step:
            return prev_num
        elif prev_step > next_step:
            return next_num
        elif prev_step < next_step:
            return prev_num

for coord in animal:
    x = findPosition(shooting, coord[0])
    if coord[1] + abs(coord[0]-x) <= L:
        count += 1

print(count)