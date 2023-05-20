from sys import stdin as s

s = open("input.txt", "rt")

A, B, C = map(int, s.readline().split())
def multiply(A, B, C):
    if B == 1:
        return A % C
    # 홀수라면
    if B % 2 == 1:
        return (multiply(A, B // 2, C) ** 2) * A % C
    # 짝수라면
    else:
        return (multiply(A, B // 2, C) ** 2) % C

print(multiply(A, B, C))