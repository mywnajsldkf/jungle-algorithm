from sys import stdin as s
from itertools import permutations

N = int(s.readline())
A = list(s.readline().split())

for i in range(N):
    A[i] = int(A[i])

problems = list(permutations(A))

max = 0

for problem in problems:
    sum = 0
    for i in range(N-1):
        sum += abs(problem[i+1]-problem[i])

    if(sum > max):
        max = sum

print(max)