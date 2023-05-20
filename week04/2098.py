from sys import stdin as s
import sys

s = open("input.txt", "rt")

n = int(s.readline())

city = []

for i in range(4):
    city.append(list(map(int, s.readline().split())))

