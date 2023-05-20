from sys import stdin as s

s = open("input.txt", "rt")
N = int(s.readline())

stack = []
for i in range(N):
    x, r = map(int, s.readline().split())
    print(x, r)