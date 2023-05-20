from sys import stdin as s
import sys
from collections import deque

s = open("input.txt", "rt")

n = int(s.readline())
now = list(map(int, s.readline().strip()))
end = list(map(int, s.readline().strip()))

