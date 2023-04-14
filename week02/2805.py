import sys
from sys import stdin as s

s = open("input.txt", "rt")

N, M = map(int, s.readline().split())

tree = list(map(int, s.readline().split()))
result = 0
def buyTree(tree, target):
    global result
    left, right = 1, max(tree)

    while(left <= right):
        total = 0
        middle = (left + right) // 2

        for height in tree:
            if (height - middle) >= 0:
                total += (height - middle)

            if total > target:
                break

        if total < target:
            right = middle - 1
        else:
            left = middle + 1
    result = right

buyTree(tree, M)
print(result)