from sys import stdin as s
from collections import deque

import sys
sys.setrecursionlimit(10**6)

s = open("input.txt", "rt")

N = int(s.readline())
number = list(map(int, s.readline().split()))
operator = list(map(int, s.readline().split()))
MAX = -sys.maxsize
MIN = sys.maxsize


def dfs(num, depth):
    global MAX, MIN

    if depth == N:
        MAX = max(num, MAX)
        MIN = min(num, MIN)
        return

    for i in range(4):
        if operator[i] > 0:
            operator[i] -= 1

            # 덧셈
            if i == 0:
                dfs(num + number[depth], depth + 1)
            # 뺄셈
            elif i == 1:
                dfs(num - number[depth], depth + 1)
            # 곱셈
            elif i == 2:
                dfs(num * number[depth], depth + 1)
            # 나눗셈
            elif i == 3:
                dfs(num // number[depth], depth + 1)

            operator[i] += 1


dfs(number[0], 1)
print(MAX)
print(MIN)
