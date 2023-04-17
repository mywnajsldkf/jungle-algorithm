from sys import stdin as s

s = open("../input.txt", "rt")

N, M = map(int, s.readline().split())
matrixA = [[0]*M]*N

for i in range(N):
    matrixA[i] = list(map(int, s.readline().split()))

M, K = map(int, s.readline().split())
matrixB = [[0]*K]*M

for i in range(M):
    matrixB[i] = list(map(int, s.readline().split()))

result = [[0]*K for _ in range(N)]

for row in range(N):
    for col in range(K):
        total = 0
        for i in range(M):
            total += matrixA[row][i] * matrixB[i][col]
        result[row][col] = total

for r in result:
    print(*r)