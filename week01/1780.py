from sys import stdin as s

N = int(s.readline())

matrix = []

for i in range(N):
    matrix.append(list(map(int, s.readline().split())))

