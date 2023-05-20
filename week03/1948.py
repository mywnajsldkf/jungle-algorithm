import heapq
from sys import stdin as s

s = open("input.txt", "rt")

n = int(s.readline())
m = int(s.readline())

graph = [[] for _ in range(n+1)]

for i in range(m):
    start, end, time = map(int, s.readline().split())
    graph[start].append()