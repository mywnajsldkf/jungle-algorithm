from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")

N = int(s.readline())
A = list(map(int, s.readline().split()))

print(A)