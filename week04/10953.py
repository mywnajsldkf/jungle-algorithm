from sys import stdin as s
import sys

s = open("input.txt", "rt")

t = int(s.readline())

for i in range(t):
    a, b = map(int, s.readline().split(","))
    print(a+b)