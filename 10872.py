from sys import stdin as s

N = int(s.readline())

result = 1

if N == 0:
    result = 1
elif N == 1:
    result = 1
else:
    for i in range(N, 1, -1):
        result *= i

print(result)