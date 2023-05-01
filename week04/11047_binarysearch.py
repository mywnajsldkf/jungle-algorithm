from sys import stdin as s
import sys

s = open("input.txt", "rt")

n, k = map(int, s.readline().split())
coin = []

for i in range(n):
    coin.append(int(s.readline()))

count = 0


def findNearest(k):
    left = 0
    right = len(coin) - 1

    # 이진탐색으로 찾음
    while left <= right:
        middle = (left + right) // 2

        if k == coin[middle]:
            return coin[middle]
        elif k < coin[middle]:
            right = middle - 1
        elif k > coin[middle]:
            left = middle + 1

    # 이진탐색으로 못 찾음
    if right <= -1:
        return coin[0]
    elif left >= len(coin):
        return coin[len(coin) - 1]
    else:
        return coin[right]


while k != 0:
    div = findNearest(k)
    count += k // div
    k = int(k % div)

print(count)