from sys import stdin as s

s = open("input.txt", "rt")

N, B = map(int, s.readline().split())  # N: 행렬크기, B:제곱횟수
matrix = [0] * N

for i in range(N):
    matrix[i] = list(map(int, s.readline().split()))


def cal(matrixA, matrixB):
    n = len(matrixA)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            total = 0
            for k in range(n):
                total += matrixA[i][k] * matrixB[k][j]
            result[i][j] = total % 1000

    return result


def square(matrix, b):
    # 행렬의 모든 원소를 1000으로 나눠준다.
    if b == 1:
        for y in range(N):
            for x in range(N):
                matrix[y][x] %= 1000
        return matrix

    # b가 짝수인 경우
    if b % 2 == 0:
        return cal(square(matrix, b // 2), square(matrix, b // 2))
    # b가 홀수인 경우
    else:
        return cal(cal(square(matrix, b // 2), square(matrix, b // 2)), matrix)


result = square(matrix, B)

for r in result:
    print(*r)
