from sys import stdin as s
import sys

s = open("input.txt", "rt")

t = int(s.readline())
boxes = list(map(int, s.readline().split()))

for i in range(1, len(boxes)):
